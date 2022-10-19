class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        number_of_messages = defaultdict(int)
        for i in range(len(messages)):
            number_of_messages[senders[i]] += messages[i].count(' ')+1
        keys = sorted(number_of_messages.keys())
        the_same_frequency = defaultdict(list)
        max_frequency = 0
        for key in keys:
            the_same_frequency[number_of_messages[key]].append(key)
            max_frequency = max(max_frequency,number_of_messages[key])
        return the_same_frequency[max_frequency][-1]
            
            