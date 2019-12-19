"""__author__=余婷"""


# 6.(尝试)写一个类，其功能是：1.解析指定的歌词文件的内容 2.按时间显示歌词 提示：歌词文件的内容一般是按下面的格式进行存储的。歌词前面对应的是时间，在对应的时间点可以显示对应的歌词
class Lyric:
    def __init__(self):
        self._time = 0
        self.word = ''

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        fen = float(value[1:3])
        miao = float(value[4:])
        self._time = fen*60 + miao

    def __repr__(self):
        return '{}:{}'.format(self.time, self.word)

    def __lt__(self, other):
        return self.time < other.time



class LyricAnalysis:

    def __init__(self, song_name: str):
        self.__song_name = song_name
        self.__lyrics = []

    def __analysis_file(self):
        # 1.读歌词文件中的内容
        with open('files/'+self.__song_name+'.lrc', 'r', encoding='utf-8') as f:
            while True:
                line_content = f.readline()
                if not line_content:
                    break

                # 将时间和词分离
                lines = line_content.split(']')
                word = lines[-1]
                for time in lines[:-1]:
                    lyric = Lyric()
                    lyric.time = time
                    lyric.word = word
                    self.__lyrics.append(lyric)

        # 对歌词进行排序
        self.__lyrics.sort(reverse=True)
        # print(self.__lyrics)
        print('解析歌词')

    def get_lyric(self, time):
        """根据时间获取歌词"""
        if not self.__lyrics:
            self.__analysis_file()

        # 找到第一个小于指定时间的歌词对象
        for lyric in self.__lyrics:
            if lyric.time <= time:
                return lyric.word


l1 = LyricAnalysis('蓝莲花')
# l1.analysis_file()
print(l1.get_lyric(100))
print(l1.get_lyric(120))

# {'00:00.20': '蓝莲花\n'}
# {'00:00.80': '没有什么能够阻挡\n'}


