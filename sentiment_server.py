import torch
from flask import abort
from preprocess import pre_process
import torch.nn.functional as F
from cnn_text import CNN_Text


STARS = [1, 2, 3, 4, 5]
STARS_SENTIMENT = {1:'negative', 2: 'negative', 3:'neutral', 4:'positive', 5:'positive'}

class SentimentService:

    def __init__(self):
        ## Model loading
        try:
            model_path='textcnn_state_dict'
            self.model = CNN_Text()
            self.model.load_state_dict(torch.load(model_path))
            
            
            #self.model = torch.jit.load(model_path, map_location='cpu')
            for param in self.model.parameters():
                param.requires_grad = False
            self.model.eval()
        except FileNotFoundError:
            abort(401, description='Model File not found')    
        except:
            abort(402, description='Unknown error') 

  


    
    def predict(self, text):
        x = pre_process(text)
        x = torch.tensor(x, dtype=torch.long)
        pred = self.model(x).detach()
        pred = F.softmax(pred).cpu().numpy()  
        pred = pred.argmax(axis=1)
        pred = STARS[pred[0]]
        return STARS_SENTIMENT[pred]


