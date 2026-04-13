==================================
 编程环境安装
==================================

介绍
-----------

用户在 PC 上通过 WIFI、 USB 和 UART 跟 EP 建立连接后，可以使用明文 SDK 跟 EP 进行通信，进行更复杂的二次开发。用户可以在 PC 上使用 C++、 C#、 Python 或是其他语言进行编程，用户可根据自身开发能力选择开发语言。

为了让用户尽快熟悉 EP 的各个模块和功能，并方便使用本网站中的 Python 示例代码，我们介绍一下 Python 在 PC 上的安装步骤。


在 Windows 上安装 Python
-------------------------

**环境：** Windows 10 64 位

1. 从python官网  `python 官网链接 <https://www.python.org/downloads/windows/>`_ 下载 **64 位 CPython 3.14 或更高版本** 安装包。

.. warning:: 本 fork 的 RoboMaster SDK 以 **CPython 3.14+** 为目标版本，请务必安装 64 位 Python。

.. image:: ./images/win_python_setup1.png


2. 步骤（1）：确认安装包版本是 ``64-bit``。

   步骤（2）：勾选 ``Add Python to PATH``。

   步骤（3）：选择 ``Install Now`` 进行安装，如下图所示。

.. image:: ./images/win_python_setup2.png


3. 安装完成后按 ``win+r``，在弹出窗口中输入 ``cmd`` 打开命令提示符界面，在命令行里面输入 ``python --version``, 确认 Python 3.14+ 安装成功。

.. image:: ./images/python_version.png

.. note:: cmd窗口会显示对应的版本信息，否则，请从第一步重新安装


在 Ubuntu 上安装 Python
-------------------------

**环境：** 64 位 Linux，Python 3.14 或更高版本

1. 请使用发行版软件源、pyenv，或官方构建安装 **Python 3.14+**。请不要卸载系统自带 Python。

2. 推荐使用虚拟环境隔离 SDK 依赖：

::

	python3.14 -m venv .venv
	source .venv/bin/activate
	python -m pip install --upgrade pip

3. 输入如下命令确认解释器版本：

::

	python --version

4. 确认命令输出为 Python 3.14 或更高版本后，再安装 RoboMaster SDK。

