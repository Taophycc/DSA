class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        mp = defaultdict(list)
        for t in transactions:
            arr = t.split(",")
            mp[arr[0]].append(arr[1:])

        invalid_id = set()
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")

            if int(amount) > 1000:
                invalid_id.add(i)

            for past_data in mp[name]:
                past_time, past_amount, past_city = past_data

                if past_city != city and abs(int(past_time) - int(time)) <= 60:
                    invalid_id.add(i)
                    break
        
        invalid_list = []
        for invalid in invalid_id:
            invalid_list.append(transactions[invalid])
        return invalid_list