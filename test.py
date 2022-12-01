import timeit


class Test:
    def __init__(self, test_times=100000):
        # 默认测试100000次

        self.test_times = test_times
        self.t_wid = 0
        self.t_deep = 0
        self.t_greed = 0
        self.t_astar = 0

    def getTotalTime(self):
        self.t_wid = timeit.timeit(stmt='gs.widthFirstSearch()',
                                   setup='from __main__ import gs',
                                   number=self.test_times)

        self.t_deep = timeit.timeit(stmt='gs.deepFirstSearch()',
                                    setup='from __main__ import gs',
                                    number=self.test_times)

        self.t_greed = timeit.timeit(stmt='gs.greedSearch()',
                                     setup='from __main__ import gs',
                                     number=self.test_times)

        self.t_astar = timeit.timeit(stmt='gs.AstarAlgorithm()',
                                     setup='from __main__ import gs',
                                     number=self.test_times)
