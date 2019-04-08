
class Configuration:
    def __init__(self, csv_path):
        with open(json_path) as json_file:
                    commentless_content = '\n'.join(map(lambda x: x[:x.find('//')], json_file.readlines()))
                    conf = json.loads(commentless_content)
                    self._conf = conf
