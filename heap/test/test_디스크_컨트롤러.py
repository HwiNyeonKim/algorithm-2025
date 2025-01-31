from heap import solution_disk_controller


def test_disk_controller():
    answer = solution_disk_controller([[0, 3], [1, 9], [2, 6]])
    assert answer == 8
