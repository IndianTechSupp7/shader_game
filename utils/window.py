import pygame
from utils.shader import DefaultScreenShader, Texture
import win32gui
import win32con


def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
    if message == win32con.WM_SIZE:
        draw_callback()
        win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
    return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)




class Window:
    def __init__(self, size=(840, 720), maximize=False, resizable=False):
        pygame.init()
        self.screen = pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE) #pygame.OPENGL | pygame.RESIZABLE | pygame.DOUBLEBUF
        pygame.display.set_caption("MyWindow")
        if maximize:
            window_handle = Call_Window.find_window("MyWindow")  # replace MyWindow with actual name as captioned.
            if window_handle:
                Call_Window.maximize_window(window_handle)
            else:
                print("Window not found.")
        self.size = self.w, self.h = self.screen.get_size()
        self.display = pygame.Surface(self.size, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()

        self.screen_shader = DefaultScreenShader(self.display)


        self.clock = pygame.time.Clock()
        self.dt = 0


        self.mouse = {
            "press" : [False, False, False],
            "release" : [False, False, False],
            "hold" : [False, False, False],
            "pos" : (0, 0),
            "rel" : (0, 0),
            "scroll_up" : False,
            "scroll_down" : False,
        }

        oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC,
                                            lambda *args: wndProc(oldWndProc, self.update, *args))

    def events(self, press = {}, release = {}):
        self.mouse["press"] = [False, False, False]
        self.mouse["release"] = [False, False, False]
        self.mouse["scroll_up"] = False
        self.mouse["scroll_down"] = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse["press"][0] = True
                    self.mouse["hold"][0] = True
                if event.button == 2:
                    self.mouse["press"][1] = True
                    self.mouse["hold"][1] = True
                if event.button == 3:
                    self.mouse["press"][2] = True
                    self.mouse["hold"][2] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse["release"][0] = True
                    self.mouse["hold"][0] = False
                if event.button == 2:
                    self.mouse["release"][1] = True
                    self.mouse["hold"][1] = False
                if event.button == 3:
                    self.mouse["release"][2] = True
                    self.mouse["hold"][2] = False
                if event.button == 4:
                    self.mouse["scroll_down"] = True
                if event.button == 5:
                    self.mouse["scroll_up"] = True
            if event.type == pygame.KEYDOWN:
                for e in press:
                    if event.key == e:
                        press[e]()
            if event.type == pygame.KEYUP:
                for e in release:
                    if event.key == e:
                        release[e]()
            if event.type == pygame.VIDEORESIZE:
                self.size = self.w, self.h = event.w, event.h
                self.display = pygame.Surface(self.size, pygame.SRCALPHA)
                self.screen_shader.set_target_texture(Texture(self.display, self.screen_shader.ctx))
                self.screen_shader.set_target_surface(self.display)


        mx, my = pygame.mouse.get_pos()
        mx /= self.screen.width/self.display.width
        my /= self.screen.height/self.display.height
        self.mouse["pos"] = (mx, my)
        self.mouse["rel"] = pygame.mouse.get_rel()

    @staticmethod
    def update(func):
        def wrapper(self):
            #self.size = self.w, self.h = self.screen.get_size()
            self.display = pygame.Surface(self.size, pygame.SRCALPHA)
            self.display.fill((100, 0, 0))
            func(self)
            self.screen_shader.set_target_texture(Texture(self.display, self.screen_shader.ctx))
            self.screen_shader.set_target_surface(self.display)
            self.screen_shader.render()
            pygame.display.flip()
        return wrapper


    def run(self):
        while True:
            #self.events()
            self.update()
            self.dt = self.clock.tick(120)/1000


class Call_Window():
    def find_window(window_title):
        # Use window title to get window's handle
        window_handle = win32gui.FindWindow(None, window_title)
        return window_handle

    def maximize_window(window_handle):
        # Get current status
        window_placement = win32gui.GetWindowPlacement(window_handle)

        # If minimized currently, restore it
        if window_placement[1] == win32con.SW_SHOWMINIMIZED:
            win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)

        # Maximize it
        win32gui.ShowWindow(window_handle, win32con.SW_MAXIMIZE)



