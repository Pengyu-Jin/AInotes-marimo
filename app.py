import marimo

__generated_with = "0.11.28"
app = marimo.App()


@app.cell
def _(mo):
    mo.md("""# Plotting a Sine Wave""")
    return


@app.cell
def _(mo, np):
    period = mo.ui.slider(start=np.pi, stop=2*np.pi, label="period")
    amplitude = mo.ui.slider(start=1, stop=2, step=0.1, label="amplitude")

    [period, amplitude]
    return amplitude, period


@app.cell
def _(amplitude, mo, period):
    mo.md(
        f"""
        Here's a plot of
        $f(x) = {amplitude.value:.02f}\sin((2\pi/{period.value:.02f}) x)$:
        """
    )
    return


@app.cell
def _(amplitude, period, plot_sine_wave):
    plot_sine_wave(period.value, amplitude.value)
    return


@app.cell
def _(np, plt):
    def plot_sine_wave(period, amplitude):
        x = np.linspace(0, 2*np.pi, num=100)
        plt.figure(figsize=(6.7, 2.5))
        plt.plot(x, amplitude*np.sin(x*2*np.pi / period))
        plt.xlabel('$x$')
        plt.xlim(0, 2*np.pi)
        plt.ylim(-2, 2)
        plt.tight_layout()
        return plt.gca()
    return (plot_sine_wave,)


@app.cell
def _():
    import marimo as mo

    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


if __name__ == "__main__":
    app.run()
