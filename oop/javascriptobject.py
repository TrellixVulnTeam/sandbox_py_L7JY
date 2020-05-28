class JavaScriptObject(dict):
    """
    JavaScript prototype and __proto__ object
    """
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)


jso = JavaScriptObject({'name': 'Hoge'})
jso.language = 'Python'
print(jso.name)
print(jso.language)
print(jso.fake)  # superのErrorも出ていることを確認する
