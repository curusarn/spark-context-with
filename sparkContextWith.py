from pyspark import SparkContext


class SparkContextWith(SparkContext):
    def __init__(self, conf):
        self.conf = conf

    def __enter__(self):
        self.sc = SparkContext(conf=self.conf)
        return self.sc

    def __exit__(self, type, value, traceback):
        self.sc.stop()
