from tile_editor import Widget



class Padding(Widget):
    RESIZE = True
    def construct_widget(self, app, parent):
        super().construct_widget(app, parent)
        #self.set_size(self.child.args.get("size") or [1, 1])
        #self.set_pos(self.child.args.get("pos") or [0, 0])
        self._set_sides(Padding.only()[1])
        self.child.get_expand()
        self._centered = False
        if self.args.get("padding"):
            name, args = self.args.get("padding")
            match name:
                case "symetric":
                    self._set_sides(self.only(args[0], args[0], args[1], args[1])[1])
                case "only":
                    self._set_sides(self.only(args[0], args[1], args[2], args[3])[1])
                case "all":
                    self._set_sides(self.only(args, args, args, args)[1])
                case "center":
                    self._set_sides(self.only(args[0], args[1], args[2], args[3])[1])
                    self._centered = True
                    self._center()



    def _handle_overload(self):
        self.expand_w = self.child.expand_w
        self.expand_h = self.child.expand_h
        if not self.child.expand_w:
            target_w = self.parent.w - self.child.w
            t = self._left + self._right
            if t:
                if t > target_w:
                    self._left = target_w * (self._left/t)
                    self._right = target_w * (self._right/t)
            self.set_width(self.child.w + (self._right + self._left))
        else:
            self.child.set_width(self.w - (self._right + self._left))

        if not self.child.expand_h:
            target_h = self.parent.h - self.child.h
            t = self._top + self._bottom
            if t:
                if t > target_h:
                    self._top = target_h * (self._top / t)
                    self._bottom = target_h * (self._bottom / t)
            self.set_height(self.child.h + (self._top + self._bottom))
        else:
            #self.set_height(self.child.h + self._bottom)
            self.child.set_height(self.h - (self._top + self._bottom))


    def _center(self):
        #print(self._left, self._right, self._top, self._bottom)

        if not self.child.expand_h:
            self.expand_h = True
            target_h = self.h - self.child.h
            t = self._top + self._bottom
            if t:
                self._top = target_h * (self._top / t)
                self._bottom = target_h * (self._bottom / t)
            else:
                self._top = self._bottom = target_h/2
        else:
            self.child.set_height(self.h - (self._top + self._bottom))

        if not self.child.expand_w:
            self.expand_w = True
            target_w = self.w - self.child.w
            t = self._left + self._right
            if t:
                self._left = target_w * (self._left / t)
                self._right = target_w * (self._right / t)
            else:
                self._left = self._right = target_w/2
        else:
            self.child.set_width(self.w - (self._right + self._left))

    def update(self):
        #super().update()
        self.child.set_pos((self._left, self._top))
        if self._centered:
            self._center()
        else:
            self._handle_overload()
        self.clear()


    def _set_sides(self, sieds):
        self._left, self._right, self._top, self._bottom = sieds


    @staticmethod
    def center(left = 0, right = 0, top = 0, bottom = 0):
        return "center", [left, right, top, bottom]

    @staticmethod
    def all(x):
        return "all", x

    @staticmethod
    def symetric(horizontal = 0, vertical = 0):
        return "symetric", (horizontal, vertical)
    @staticmethod
    def only(left = 0, right = 0, top = 0, bottom = 0):
        return "only", [left, right, top, bottom]

