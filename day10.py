import unittest

def look_and_say(n):
    repetitions = 0
    last_value = n[0] 
    summary = ""
    for i, c in enumerate(str(n)):
        # print "i:",i,'c:',c,'repetitions:',repetitions
        if c == last_value or i == 0:
            repetitions += 1
            continue
        summary += "{}{}".format(repetitions, last_value)
        last_value = c
        repetitions = 1
        # print summary
    summary += "{}{}".format(repetitions, last_value)
    return summary

def look_and_say_n_times(n, times):
    for _ in range(times):
        n = look_and_say(n)
    return n

print len(look_and_say_n_times('3113322113', 50))

class TestLookAndSay(unittest.TestCase):
    def test_single_execution(self):
        self.assertEqual(look_and_say('211'), '1221')
        self.assertEqual(look_and_say('1211'), '111221')

    def test_iterative_execution(self):
        self.assertEqual(look_and_say_n_times('1', 5), '312211')

if __name__ == "__main__":
    unittest.main()

