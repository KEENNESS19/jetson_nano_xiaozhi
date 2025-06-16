from src.utils.logging_config import get_logger
from abc import ABC, abstractmethod
from typing import Optional, Callable
import logging
import asyncio
import threading
import time

class BaseDisplay(ABC):
    """显示接口的抽象基类"""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.volume_controller = None
        # 检查音量控制依赖
        try:
            from src.utils.volume_controller import VolumeController
            if VolumeController.check_dependencies():
                self.volume_controller = VolumeController()
                self.logger.info("音量控制器初始化成功")
                # 读取系统当前音量
            else:
                self.logger.warning("音量控制依赖不满足，将使用默认音量控制")
        except Exception as e:
            self.logger.warning(f"音量控制器初始化失败: {e}，将使用模拟音量控制")

    @abstractmethod
    def set_callbacks(self,
                      press_callback: Optional[Callable] = None,
                      release_callback: Optional[Callable] = None,
                      status_callback: Optional[Callable] = None,
                      text_callback: Optional[Callable] = None,
                      mode_callback: Optional[Callable] = None,
                      auto_callback: Optional[Callable] = None,
                      abort_callback: Optional[Callable] = None,
                      send_text_callback: Optional[Callable] = None):  # 添加打断回调参数
        """设置回调函数"""
        pass

    @abstractmethod
    def update_status(self, status: str):
        """更新状态文本"""
        pass

    @abstractmethod
    def update_text(self, text: str):
        """更新TTS文本"""
        pass

    @abstractmethod
    def start(self):
        """启动显示"""
        pass

    @abstractmethod
    def on_close(self):
        """关闭显示"""
        pass

    @abstractmethod
    def start_button_listener(self):
        """启动按钮监听"""
        pass

    @abstractmethod
    def stop_button_listener(self):
        """停止按钮监听"""
        pass

class CliDisplay(BaseDisplay):
    def __init__(self):
        super().__init__()  # 调用父类初始化
        """初始化CLI显示"""
        self.logger = get_logger(__name__)
        self.running = True
        
        # 状态相关
        self.current_status = "未连接"
        self.current_text = "待命"

        # 回调函数
        self.auto_callback = None
        self.status_callback = None
        self.text_callback = None
        self.abort_callback = None
        self.send_text_callback = None
        
        # 状态缓存
        self.last_status = None
        self.last_text = None

        # 为异步操作添加事件循环
        self.loop = asyncio.new_event_loop()

    def set_callbacks(self,
                      press_callback: Optional[Callable] = None,
                      release_callback: Optional[Callable] = None,
                      status_callback: Optional[Callable] = None,
                      text_callback: Optional[Callable] = None,
                      mode_callback: Optional[Callable] = None,
                      auto_callback: Optional[Callable] = None,
                      abort_callback: Optional[Callable] = None,
                      send_text_callback: Optional[Callable] = None):
        """设置回调函数"""
        self.status_callback = status_callback
        self.text_callback = text_callback
        self.auto_callback = auto_callback
        self.abort_callback = abort_callback
        self.send_text_callback = send_text_callback

    def update_status(self, status: str):
        """更新状态文本"""
        if status != self.current_status:
            self.current_status = status
            self._print_current_status()

    def update_text(self, text: str):
        """更新TTS文本"""
        if text != self.current_text:
            self.current_text = text
            self._print_current_status()

    def start_button_listener(self):
        '''启动按钮监听'''
        pass

    def stop_button_listener(self):
        '''停止按钮监听'''
        pass

    def start(self):
        # 启动状态更新线程
        self.start_update_threads()

        # 主循环
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.on_close()

    def on_close(self):
        """关闭CLI显示"""
        self.running = False
        print("\n正在关闭应用...")

    def start_update_threads(self):
        """启动更新线程"""
        def update_loop():
            while self.running:
                try:
                    # 更新状态
                    if self.status_callback:
                        status = self.status_callback()
                        if status and status != self.current_status:
                            self.update_status(status)

                    # 更新文本
                    if self.text_callback:
                        text = self.text_callback()
                        if text and text != self.current_text:
                            self.update_text(text)

                except Exception as e:
                    self.logger.error(f"状态更新错误: {e}")
                time.sleep(0.1)

        # 启动更新线程
        threading.Thread(target=update_loop, daemon=True).start()

    def _print_current_status(self):
        """打印当前状态"""
        # 检查是否有状态变化
        status_changed = (
            self.current_text != self.last_text 
        )
        status_changed_status = (
            self.current_status != self.last_status
        )

        if status_changed:
            print("\n=== 当前状态 ===")
            print(f"状态: {self.current_status}")
            print(f"文本: {self.current_text}")
            print("===============\n")

            # 更新缓存
            self.last_status = self.current_status
            self.last_text = self.current_text