#  complejidad algoritmica
#  https://docs.bokeh.org/en/latest/index.html
#  https://stackoverflow.com/questions/62814002/start-this-command-cannot-be-run-due-to-the-error-the-system-cannot-find-the

from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("graficado_simple.html")
    fig = figure()

    total_vals = int(input("Cuantos valores quieres graficar?"))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f"Valor y para {x}"))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
