


| Flag              | Description                                                                                                                                      | Example              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| `-a`, `--append`  | Add one or more suffixes                                                                                                                         | `-a 2023 2024 2025!` |
| `-p`, `--prepend` | Add one or more prefixes                                                                                                                         | `-p admin user`      |
| `-H`              | Convert to **UPPERCASE**                                                                                                                         | `-H`                 |
| `-L`              | Convert to **lowercase**                                                                                                                         | `-L`                 |
| `-C`              | Capitalize each word (first letter uppercase)                                                                                                    | `-C`                 |
| `-H1`             | Uppercase **only the first letter** (e.g. `hello` → `Hello`)                                                                                     | `-H1`                |
| `-L2`             | Lowercase **only the first letter** (e.g. `Hello` → `hello`)                                                                                     | `-L2`                |
| `-All`            | Generate **both** variants for each word: one with first letter uppercase and one with first letter lowercase (e.g. `Hello2023` and `hello2023`) | `-All`               |
| `-r`              | Reverse each word                                                                                                                                | `-r`                 |



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
