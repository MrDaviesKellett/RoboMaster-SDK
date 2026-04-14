.. _installs:

#############################
RoboMaster SDK 安装
#############################




安装 SDK 到 Windows平台
-------------------------

开发环境准备
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip:: 在使用python sdk前，需要确保编程平台端安装对应的python环境，建议参考以下链接进行安装或重新安装： :doc:`python编程环境安装 <./../code_env_setup>`

安装VC库环境（可选）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

下载（`下载地址：GitHub RoboMaster SDK repository <https://github.com/dji-sdk/robomaster-sdk>`_ , `备用地址：Gitee RoboMaster SDK repository <https://gitee.com/xitinglin/RoboMaster-SDK>`_）安装VC库的exe可执行文件：

.. image:: ./../images/vc_exe.png

.. warning:: 如果使用SDK，出现以下问题，请执行此安装:

	.. image:: ./../images/libmedia_err.png

安装VC build tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

下载（`下载地址：GitHub RoboMaster SDK repository <https://github.com/dji-sdk/robomaster-sdk>`_ , `备用地址：Gitee RoboMaster SDK repository <https://gitee.com/xitinglin/RoboMaster-SDK>`_）安装VC build tools的exe可执行文件：

.. image:: ./../images/vs_build_tool.png

.. warning:: 不安装VC build tools，安装SDK,会报以下错误：

	.. image:: ./../images/neti_err.jpg

安装robomaster python sdk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

安装发布到 PyPI 的本 fork 版本，点开开始菜单，在搜索框中输入 ``cmd`` ，在搜索结果中，对着命令提示符程序，单击鼠标右键，菜单中点击选择 ``以管理员身份运行`` ，并输入以下指令::

    python -m pip install robomaster-sdk-modern

默认情况下，PyPI 提供的平台 wheel 将直接包含 ``libmedia_codec`` ，可直接使用音视频流功能。
   
如果网络较差，多次都安装失败，可以尝试::

    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple robomaster-sdk-modern

如需直接从当前仓库源码安装，可在仓库根目录执行::

    python -m pip install .

如需运行二维码联网辅助示例，可额外安装::

    python -m pip install MyQR

如果 pip 因平台原因退回源码构建，标准安装流程也会自动编译 ``libmedia_codec`` 。
如需手动兼容旧流程，仍可执行::

    python setup_with_lib.py build_ext --inplace

.. tip:: 如果出现下列情况，请参考以下链接进行python环境安装：:doc:`python编程环境安装 <./../code_env_setup>`

	.. image:: ./../images/pip_install_error.jpg

升级 RoboMaster SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当需要升级 RoboMaster SDK时，可在命令行中输入以下指令::

    python -m pip install --upgrade robomaster-sdk-modern



安装 SDK 到 Linux平台
----------------------


Linux



Python 环境安装


请先准备 Python 3.14+ 环境。


安装 RoboMaster SDK


安装 RoboMaster SDK，可输入以下指令::

    python -m pip install robomaster-sdk-modern

如无匹配 wheel，pip 会按源码包自动编译 ``libmedia_codec`` ，因此需要本机安装 CMake、pybind11 以及 FFmpeg/Opus 开发库。



升级 RoboMaster SDK


当需要升级 RoboMaster SDK时，可在命令行中输入以下指令::

    python -m pip install --upgrade robomaster-sdk-modern

.. tip:: 树莓派下的python sdk安装教程可参考 `sdk install on Raspberry Pi.7z <https://github.com/dji-sdk/robomaster-sdk>`_

安装 SDK 到 macOS X平台
---------------------------


安装 RoboMaster SDK


安装RoboMaster SDK，可输入以下指令::

    python -m pip install robomaster-sdk-modern

如无匹配 wheel，pip 会按源码包自动编译 ``libmedia_codec`` ，因此需要本机安装 CMake、pybind11 以及 FFmpeg/Opus 开发库。


升级 RoboMaster SDK


当需要升级 RoboMaster SDK时，可在命令行中输入以下指令::

    python -m pip install --upgrade robomaster-sdk-modern
