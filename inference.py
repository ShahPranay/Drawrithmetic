import io
import numpy
from numpy.core.fromnumeric import shape
import torch
from PIL import Image,ImageOps
from models import DigitsClassifier,InfixClassifier,OperatorClassifier
import torchvision.transforms as transforms

def predict_image(image_bytes):
    if torch.cuda.is_available():  
        dev = "cuda:0" 
    else:  
        dev = "cpu"
    pipclassifier = InfixClassifier().to(torch.device(dev))
    digitai = DigitsClassifier().to(torch.device(dev))
    operatorsai = OperatorClassifier().to(torch.device(dev))
    pipclassifier.load_state_dict(torch.load("./trained_models/pipclassifier.pt",map_location=torch.device(dev)))
    digitai.load_state_dict(torch.load('./trained_models/digitai.pt',map_location=torch.device(dev)))
    operatorsai.load_state_dict(torch.load('./trained_models/operatorsai.pt',map_location=torch.device(dev)))
    pipclassifier.eval()
    digitai.eval()
    operatorsai.eval()
    t = transforms.Compose([transforms.Resize(28)])
    imgbuf=io.BytesIO(image_bytes)
    img = ImageOps.grayscale(Image.open(imgbuf))
    img = t(img)
    img1 = (transforms.ToTensor()(numpy.array(img.crop((0,0,28,28))))).to(torch.device(dev))
    img2 = (transforms.ToTensor()(numpy.array(img.crop((28,0,56,28))))).to(torch.device(dev))
    img3 = (transforms.ToTensor()(numpy.array(img.crop((56,0,84,28))))).to(torch.device(dev))
    if torch.argmax(pipclassifier(img1.view(1,1,28,28))) == 1:
        type='prefix'
        no1=torch.argmax(digitai(img2.view(1,1,28,28)))
        no2=torch.argmax(digitai(img3.view(1,1,28,28)))
        opid=torch.argmax(operatorsai(img1.view(1,1,28,28)))
    elif torch.argmax(pipclassifier(img2.view(1,1,28,28))) == 1:
        type='infix'
        no1=torch.argmax(digitai(img1.view(1,1,28,28)))
        no2=torch.argmax(digitai(img3.view(1,1,28,28)))
        opid=torch.argmax(operatorsai(img2.view(1,1,28,28)))
    else:
        type='postfix'
        no1=torch.argmax(digitai(img1.view(1,1,28,28)))
        no2=torch.argmax(digitai(img2.view(1,1,28,28)))
        opid=torch.argmax(operatorsai(img3.view(1,1,28,28)))
    no1=no1.cpu()
    no2=no2.cpu()
    if opid==0:
        value = no1+no2
    elif opid == 1:
        value = no1-no2
    elif opid == 2:
        value = no1*no2
    else:
      if no2!=0:
        value = no1/no2
      else:
        value=no1
    value = value.item()
    op=['+','-','x','/']
    print(no1,op[opid],no2)
    return value

