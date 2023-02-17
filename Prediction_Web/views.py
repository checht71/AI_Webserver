"""
This is the biggest issue right here. We are working with a CNN, yet this tutorial is
implemented on a linear regression model!!!

"""

from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(pclass):
    import pickle
    model = pickle.load(open("model.sav", "rb"))
    prediction = model.predict([[pclass]])
    
    if prediction == 0:
        return "No Crack Detected"
    elif prediction == 1:
        return "Crack Detected"
    else:
        return "error"
        

# our result page view
def result(request):
    pclass = int(request.GET['pclass'])

    result = getPredictions(pclass)

    return render(request, 'result.html', {'result':result})