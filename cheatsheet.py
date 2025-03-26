import marimo

__generated_with = "0.11.28"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Numpy Cheatsheet

        np.arange(start, end, size)返回一个有终点和起点的固定步长的排列

        np.zeros(size)返回来一个给定形状用0填充的数组

        np.clip(array, min, max) 限制范围

        np.where(condition, x, y) 筛选条件为True的元素修改为x，为False的元素修改为y
        """
    )
    return


@app.cell
def _():
    import numpy as np

    ls = np.arange(10)
    print(ls)
    x = np.zeros(10)
    print(x)
    mask = (ls >= 3) & (ls < 8)
    print(mask)
    x[mask] = ls[mask] * 2
    print(x)

    x = np.where(mask, np.clip(x, 9, 11), -200)
    print(x)
    return ls, mask, np, x


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Pandas Cheatsheet

        pd.DataFrame({...}) 字典创建，key是colomn名称，value是数组，表示每列数据
        """
    )
    return


@app.cell
def _():
    import pandas as pd

    data = pd.DataFrame(
        {"Site": ["Google", "Github", "Wiki"], "Age": [10, 23, 33]}
    )

    data.to_csv("test.csv", index=False)
    print(data)
    return data, pd


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
