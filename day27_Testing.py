def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []


# complete this function

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        #return [3,1,2]
        return [6,5,4]

    # complete this function

    @staticmethod
    def get_expected_result():
        return 2

# complete this function

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        #return [3,1,1]
        return [5,5,6]
    # complete this function

    @staticmethod
    def get_expected_result():
        return 0
# complete this function


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

if __name__ == '__main__':
    TestWithEmptyArray()
    TestWithUniqueValues()
    TestiWithExactyTwoDifferentMinimums()
    print("OK")

