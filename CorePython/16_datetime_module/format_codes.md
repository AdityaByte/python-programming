# Python `strftime` Format Codes

| Code | Example | Description |
|------|---------|-------------|
| `%a` | Sun | Weekday as locale’s abbreviated name. |
| `%A` | Sunday | Weekday as locale’s full name. |
| `%w` | 0 | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. |
| `%d` | 08 | Day of the month as a zero-padded decimal number. |
| `%-d` | 8 | Day of the month as a decimal number. *(Platform specific)* |
| `%b` | Sep | Month as locale’s abbreviated name. |
| `%B` | September | Month as locale’s full name. |
| `%m` | 09 | Month as a zero-padded decimal number. |
| `%-m` | 9 | Month as a decimal number. *(Platform specific)* |
| `%y` | 13 | Year without century as a zero-padded decimal number. |
| `%Y` | 2013 | Year with century as a decimal number. |
| `%H` | 07 | Hour (24-hour clock) as a zero-padded decimal number. |
| `%-H` | 7 | Hour (24-hour clock) as a decimal number. *(Platform specific)* |
| `%I` | 07 | Hour (12-hour clock) as a zero-padded decimal number. |
| `%-I` | 7 | Hour (12-hour clock) as a decimal number. *(Platform specific)* |
| `%p` | AM | Locale’s equivalent of AM or PM. |
| `%M` | 06 | Minute as a zero-padded decimal number. |
| `%-M` | 6 | Minute as a decimal number. *(Platform specific)* |
| `%S` | 05 | Second as a zero-padded decimal number. |
| `%-S` | 5 | Second as a decimal number. *(Platform specific)* |
| `%f` | 000000 | Microsecond as a decimal number, zero-padded to 6 digits. |
| `%z` | +0000 | UTC offset in ±HHMM format (empty if naive). |
| `%Z` | UTC | Time zone name (empty if naive). |
| `%j` | 251 | Day of the year as a zero-padded decimal number. |
| `%-j` | 251 | Day of the year as a decimal number. *(Platform specific)* |
| `%U` | 36 | Week number of the year (Sunday first) as zero-padded. |
| `%-U` | 36 | Week number of the year (Sunday first). *(Platform specific)* |
| `%W` | 35 | Week number of the year (Monday first) as zero-padded. |
| `%-W` | 35 | Week number of the year (Monday first). *(Platform specific)* |
| `%c` | Sun Sep 8 07:06:05 2013 | Locale’s date and time representation. |
| `%x` | 09/08/13 | Locale’s date representation. |
| `%X` | 07:06:05 | Locale’s time representation. |
| `%%` | % | A literal `%` character. |
