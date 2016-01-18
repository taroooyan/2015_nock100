# coding: UTF-8
def return_string(x, y, z):
    return "%d時の%sは%.1f" % (x, y, z)

if __name__ == "__main__":
    print return_string(12, "気温", 22.4)
