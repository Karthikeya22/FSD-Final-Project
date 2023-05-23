import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,3))
    plt.title('price on perticular month')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('month')
    plt.ylabel('price')
    plt.tight_layout()
    graph=get_graph()
    return graph

def get_plot1(x1,y1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,3))
    plt.title('demand on perticular month')
    plt.plot(x1,y1)
    plt.xticks(rotation=45)
    plt.xlabel('month')
    plt.ylabel('demand')
    plt.tight_layout()
    graph1=get_graph()
    return graph1