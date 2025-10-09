

```

-a, --append	Add one or more suffixes	-a 2023 2024 2025!
-p, --prepend	Add one or more prefixes	-p admin user
-H	Convert to UPPERCASE	-H
-L	Convert to lowercase	-L
-C	Capitalize each word	-C
-r	Reverse each word	-r


```


## 5. Examples

Append values:

```bash
./mutator.py -w list.txt -o out.txt -a 2023 2024 2025!
```

Prepend prefixes:

```bash
./mutator.py -w list.txt -o out.txt -p admin user
```

Combine prepend + append + uppercase:

```bash
./mutator.py -w list.txt -o out.txt -p admin user -a 2023 2024! -H
```
