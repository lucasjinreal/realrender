# RealRender

RealRender, aka RR, is a new library for 3D rendering visualization. Previously visualizer lib are **really confusing**, like OpenDR, pyrender, pytorch3d etc, I still don't know why pytorch3d CPU so slow. And some lib claims they implement in OpenGL like opendr, but their **speed are not likely used OpenGL**, just too slow to render.

So I decided pave my own way. RealRender is a 3D render lib that focus on **Speed**, however, there still need more test on various platforms and hardware, currently, RealRender used a new render lib that runs **fastest on my mac**. Other platform still need to test.

## Install

You can using:

```
pip install realrender
```

Or install from source:

```
python setup.py build develop
```

## Result

Here are some results that renders face mesh and human mesh. **it's so simple to use realrender**.

![](https://s4.ax1x.com/2022/02/12/HBpbY6.png)

![](https://s4.ax1x.com/2022/02/20/HLGD00.gif)


## Copyright

Codes released under GPL-v2 license. All rights reserved by Lucas Jin.