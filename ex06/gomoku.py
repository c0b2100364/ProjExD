import tkinter
import tkinter.messagebox


# キャンバスの縦横サイズ
canv_size = 400

# ラインの数
line_num = 10

# 色設定
BAN_COLOR = 'burlywood3' # 盤面の背景
P1_COLOR = 'black' # プレイヤー1の石の色
P2_COLOR = 'white' # プレイヤー2の石の色

# プレイヤーを示す値
P_ONE = 1
P_TWO = 2

class Gomoku():
    def __init__(self, oya):
        self.oya = oya # 親ウィジェット
        self.player = P_ONE # 次におく石の色
        self.board = None # 盤面情の意思を管理する二次元リスト
        self.color = {P_ONE : P1_COLOR, P_TWO : P2_COLOR} # 石の色を保持する辞書
        self.nextDisk = None
        
        #ウィジェットの作成
        self.make_wid()

        # イベントの設定
        self.set_event()

        # 五目並べの初期化
        self.init_gomoku()


    def make_wid(self):

        # キャンバスの作成
        self.canv = tkinter.Canvas(
            self.oya, bg = BAN_COLOR, width = canv_size,
            height = canv_size, highlightthickness = 0
        )
        self.canv.pack(padx = 10, pady = 10)


    def set_event(self):

        # キャンバス上でマウスクリックを受け付ける
        self.canv.bind('<ButtonPress>', self.click)


    def init_gomoku(self):

        # 盤面上の石を管理する2次元リストの作成
        self.board = [[None] * (line_num) for i in range(line_num)]

        # 線の間隔を計算
        self.kan = canv_size // (line_num + 1)

        # 交点描画位置の上下オフセット
        self.offset_x = self.kan
        self.offset_y = self.kan

        # 縦線の描画
        for j in range(line_num):

            # 線の開始と終了の座標計算
            start_x = j * self.kan + self.offset_x
            start_y = self.offset_y
            end_x = start_x
            end_y = (line_num - 1) * self.kan + self.offset_y

            # 線を描画
            self.canv.create_line(start_x, start_y, end_x, end_y)

        # 横線の描画
        for k in range(line_num):

            # 線の開始と終了座標計算
            start_x = self.offset_x
            start_y = k * self.kan + self.offset_y
            end_x = (line_num - 1) * self.kan + self.offset_x
            end_y = start_y

            # 線を描画
            self.canv.create_line(start_x, start_y, end_x, end_y)

    
    def dr_disk(self, x, y, color):

        # (x,y)の交点の中心座標を計算
        center_x = x * self.kan + self.offset_x
        center_y = y * self.kan + self.offset_y

        # 中心座標からの円の開始と終了座標を計算
        start_x = center_x - (self.kan * 0.8) // 2
        start_y = center_y - (self.kan * 0.8) // 2
        end_x = center_x + (self.kan * 0.8) // 2
        end_y = center_y + (self.kan * 0.8) // 2

        # 円を描画する
        name_tag = 'disk_' + str(x) + '_' + str(y)
        self.canv.create_oval(start_x, start_y, end_x, end_y, fill = color)

        return name_tag


    def get_intersec(self, x, y):
        inter_x = (x - self.offset_x + self.kan // 2) // self.kan
        inter_y = (y - self.offset_y + self.kan // 2) // self.kan

        return inter_x, inter_y


    def click(self, event):
        
        if self.player != P_ONE:
            return
         
        # クリックされた位置がどの交点か計算
        x, y = self.get_intersec(event.x, event.y)

        if x < 0 or x >= line_num or y < 0 or y >= line_num:
            return

        if not self.board[y][x]:

            self.place(x, y, self.color[self.player])

    
    def place(self, x, y, color):
        #(x,y)に石を置く
        self.dr_disk(x, y, color)

        # 描画した円の色を管理リストに記憶させる
        self.board[y][x] = color

        # 5つ並んだかどうかチェック
        if self.count(x, y, color) >= 5:
            self.show_res()
            return

        # プレイヤーは交互に変更
        if self.player == P_TWO:
            self.player = P_ONE
        else:
            self.player = P_TWO


    
    def count(self, x, y, color):

        count_dir = [(1, 0)#右,
                    , (1, 1)#右下
                    , (0, 1)#上
                    , (-1, 1)#左下
                    ]
        
        max = 0 # 石の並び数最大値


        for i, j in count_dir:

            count_num = 1

            for k in range(1, line_num):

                xi = x + i * k
                yj = y + j * k

                if xi < 0 or xi >= line_num or yj < 0 or yj >= line_num:
                    # 盤面外の交点の場合は石は連続していない
                    break

                if self.board[yj][xi] != color:
                    # 異なる色の石が置かれていれば石は連続していない
                    break

                count_num += 1

            for k in range(-1, -(line_num), -1):
                xi = x + i * k
                yj = y + j * k

                if xi < 0 or xi >= line_num or yj < 0 or yj >= line_num:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1


            if max < count_num:
                max = count_num

        return max
    

    def show_res(self):

        winner = self.player

        if winner == P_ONE:
            tkinter.messagebox.showinfo('結果', 'Player1の勝ちです')
        else:
            tkinter.messagebox.showinfo('結果', 'Player2の勝ちです')
    

if __name__ == "__main__":
    app = tkinter.Tk()
    app.title('五目並べ')
    gobang = Gomoku(app)
    app.mainloop()
