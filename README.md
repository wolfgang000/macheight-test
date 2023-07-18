### Run app

```sh
python app.py 1,9,5,0,20,-4,12,16,7 12
```

### Run tests

```sh
python tests.py
```

`find_pairs` uses a binary search to find the pairs, since the order of the pairs doesn't matter we only need to iterate over half the array to get the list of pair combinations, it has a complexity of O((n/2) * log(n))  

To order the array we use the python's `sorted` funtion it has a complexity of O(n * log(n)) 