# RealRender

RealRender, aks RR, is a new library for 3D rendering visualization. Previously visualizer lib are **really confusing**, like OpenDR, pyrender, pytorch3d etc, I still don't know why pytorch3d CPU so slow. And some lib claims they implement in OpenGL like opendr, but their **speed are not likely used OpenGL**, just too slow to render.

So I decided pave my own way. RealRender is a 3D render lib that focus on **Speed**, however, there still need more test on various platforms and hardware, currently, RealRender used a new render lib that runs **fastest on my mac**. Other platform still need to test.


## Result

Here are some results that renders face mesh and human mesh. **it's so simple to use realrender**.

