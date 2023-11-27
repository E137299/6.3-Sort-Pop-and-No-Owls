from main import *

def test_sort_and_clip():
    assert sort_and_clip([10,5,3,8,12,4,2]) == [3,4,5,8,10]
    assert sort_and_clip([-10,11,3,-5,99,61]) == [-5,3,11,61]

def test_outliers():
    assert outliers([10,4,8,7,12,15,-1,-1],0,10) == [4,7,8]
    assert outliers([20,21,22,23,24,25,26,27,28,29],23,27) == [23,24,25,26,27]

def test_no_owls(list):
    assert no_owls(["bowl","howl","acknowledge","waterfowl","growl"]) == ["birdl","birdl","acknbirdedge","waterfbird","grbird"]
    assert no_owls(["meadowlark","scowl","shadowless","lowland","lowlight"]) == ["meadbirdark","scbird","shadbirdess","lbirdand","lbirdight"]
