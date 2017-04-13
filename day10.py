import unittest

def look_and_say(s):
    repetitions = 0
    last_seen = s[0]
    said = ""
    for i, ch in enumerate(s):
        if ch == last_seen or i == 0:
            repetitions += 1
            continue
        said += str(repetitions) + str(last_seen)
        last_seen = ch
        repetitions = 1
    said += str(repetitions) + str(last_seen)
    return said

def look_and_say_n_times(s, times):
    for _ in xrange(times):
        s = look_and_say(s)
    return s

class TestLookAndSay(unittest.TestCase):
    def test_single_execution(self):
        self.assertEqual(look_and_say('211'), '1221')
        self.assertEqual(look_and_say('1211'), '111221')

    def test_iterative_execution(self):
        self.assertEqual(look_and_say_n_times('1', 5), '312211')

# print len(look_and_say_n_times('3113322113', 50))

if __name__ == "__main__":
    unittest.main()
