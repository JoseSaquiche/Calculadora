from django.shortcuts import render
import numpy as np 

def secante(request):
    resultados = []
    ecuacion = ""
    if request.method == "POST":
        ecuacion = request.POST.get("ecuacion")
        x0 = float(request.POST.get("x0", 1))  # Puedes pedir estos valores en el formulario
        x1 = float(request.POST.get("x1", 2))
        tol = 1e-6
        max_iter = 20

        # Convierte la ecuación en una función de Python
        def f(x):
            return eval(ecuacion, {"x": x, "np": np, "__builtins__": {}})

        for n in range(1, max_iter+1):
            fx0 = f(x0)
            fx1 = f(x1)
            if fx1 - fx0 == 0:
                break
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            error = abs(x2 - x1)
            resultados.append({
                'n': n,
                'xn_1': x0,
                'xn': x1,
                'fxn_1': fx0,
                'fxn': fx1,
                'xn1': x2,
                'error': error,
            })
            if error < tol:
                break
            x0, x1 = x1, x2

    return render(request, "secante.html",{'resultados': resultados, 'ecuacion': ecuacion})

def index(request):
    return render(request,"index.html")

def newton(request):
    resultados = []
    ecuacion =""
    if request.method == "POST":
      ecuacion = request.POST.get("ecuacion")
      derivada = request.POST.get("derivada")
      x0 = float(request.POST.get("x0",1))
      tol = 1e-6
      max_iter = 20      
    
      def f(x):
           return eval(ecuacion, {"x": x, "np": np, "__builtins__":{}})
      def df(x):
          return eval(derivada, {"x": x, "np": np, "__builtins__":{}})
      for n in range(1, max_iter+1):
        fx0 = f(x0)
        dfx0 = df(x0)
        if dfx0 == 0:
            resultados.append({'error':'la derivada es cero, no se puede resolver'})
            break
        x1 = x0 - fx0 / dfx0
        error = abs(x1 - x0)
        resultados.append({
            'n': n,
            'xn': x0,
            'fxn': fx0,
            'dfxn': dfx0,
            'xn1': x1,
            'error': error,
        })
        if error < tol:
            break
        x0 = x1

    return render(request, "newton.html", {'resultados': resultados,'ecuacion':ecuacion})   

def biseccion(request): 
    resultados = []
    ecuacion=""
    if request.method == "POST":
       ecuacion = request.POST.get("ecuacion")
       a = float(request.POST.get("a",0))
       b= float(request.POST.get("b",1))
       tol = 1e-6
       max_iter = 20

       def f(x):
           return eval(ecuacion, {"x": x, "np":np, "__builtins__":{}})
       if f(a) * f(b) >= 0:
        resultados.append({'error': 'f(a) y f(b) deben tener signos opuestos.'})
       else:
        for n in range(1, max_iter+1):
            m = (a +b) /2
            fa = f(a)
            fb = f(b)
            fm = f(m)
            error = abs(b - a)/2
            resultados.append({
                'n': n,
                'a': a,
                'b': b,
                'm': m,
                'fa': fa,
                'fb': fb,
                'fm': fm,
                'error': error,
            })
            if abs(fm) <tol or error <tol:
                break
            if fa * fm < 0:
                b = m
            else:
                a = m

    return render(request,"biseccion.html", {'resultados':resultados,'ecuacion': ecuacion})

def newton_modificado(request):
    resultados = []
    ecuacion = ""
    derivada = ""
    if request.method == "POST":
        ecuacion = request.POST.get("ecuacion")
        derivada = request.POST.get("derivada")
        x0 = float(request.POST.get("x0", 1))
        tol = 1e-6
        max_iter = 20

        def f(x):
            return eval(ecuacion, {"x": x, "np": np, "__builtins__": {}})
        def df(x):
            return eval(derivada, {"x": x, "np": np, "__builtins__": {}})

        dfx0 = df(x0)  # Solo se calcula una vez
        if dfx0 == 0:
            resultados.append({'error': 'La derivada es cero, no se puede resolver'})
        else:
            for n in range(1, max_iter + 1):
                fx0 = f(x0)
                x1 = x0 - fx0 / dfx0
                error = abs(x1 - x0)
                resultados.append({
                    'n': n,
                    'xn': x0,
                    'fxn': fx0,
                    'dfxn': dfx0,
                    'xn1': x1,
                    'error': error,
                })
                if error < tol:
                    break
                x0 = x1

    return render(request, "newton_modificado.html", {
        'resultados': resultados,
        'ecuacion': ecuacion,
        'derivada': derivada
    })