# CHANGELOG

<!-- version list -->

## v3.32.0 (2026-08-20)

### Bug Fixes

- Address charging hub power sensor issues
  ([#2821](https://github.com/worgarside/home-assistant/pull/2821),
  [`8993c40`](https://github.com/worgarside/home-assistant/commit/8993c404ee1aa3be4857861d005bfbdc86b60480))

- Retain corroborated kitchen presence
  ([#2822](https://github.com/worgarside/home-assistant/pull/2822),
  [`1f07313`](https://github.com/worgarside/home-assistant/commit/1f0731306935bfe7599b85c8d2e628d71741c5d7))

- Update notification logic for attachments
  ([#2817](https://github.com/worgarside/home-assistant/pull/2817),
  [`4883c4c`](https://github.com/worgarside/home-assistant/commit/4883c4c0d3ad39a53d3e6e79337e7aa3eff752ba))

- **automation**: Debounce VaultPi publisher outages
  ([#2836](https://github.com/worgarside/home-assistant/pull/2836),
  [`88d1e2a`](https://github.com/worgarside/home-assistant/commit/88d1e2ad0350db8ab0b9bf507f2e1b7edefd585c))

- **binary-sensor**: Retain dining presence during FP2 dropouts
  ([#2840](https://github.com/worgarside/home-assistant/pull/2840),
  [`76fc93e`](https://github.com/worgarside/home-assistant/commit/76fc93e1e11787af46f422803506b46ed6e9d76c))

### Chores

- Remove desmond cam usage in automation
  ([#2842](https://github.com/worgarside/home-assistant/pull/2842),
  [`934a27e`](https://github.com/worgarside/home-assistant/commit/934a27e3f2a46b6fdd74128e83a75e7e6117fc50))

- Remove unused luci device tracker
  ([#2841](https://github.com/worgarside/home-assistant/pull/2841),
  [`09ea986`](https://github.com/worgarside/home-assistant/commit/09ea98686607f577c4a530a4e30e0f8bbd578418))

- Remove unused Spotify Tempo variable
  ([#2838](https://github.com/worgarside/home-assistant/pull/2838),
  [`a80359f`](https://github.com/worgarside/home-assistant/commit/a80359fe0ecbb27aaf28f72a3404771ef10ea775))

- **sync**: Pin github-config-files workflows to 0.3.3
  ([#2823](https://github.com/worgarside/home-assistant/pull/2823),
  [`5ba2d7c`](https://github.com/worgarside/home-assistant/commit/5ba2d7c795d0f7e276778d37959efd9e0b395ba5))

- **sync**: Pin github-config-files workflows to 0.5.3
  ([#2829](https://github.com/worgarside/home-assistant/pull/2829),
  [`237b7a7`](https://github.com/worgarside/home-assistant/commit/237b7a7bf0159842a3b9ec47d8bb4830fd0b83c2))

### Continuous Integration

- Prek autoupdate ([#2835](https://github.com/worgarside/home-assistant/pull/2835),
  [`6128821`](https://github.com/worgarside/home-assistant/commit/612882190548b2dc8aedeb0f86d5e2ccc2708656))

- Update prek hooks ([#2824](https://github.com/worgarside/home-assistant/pull/2824),
  [`7699125`](https://github.com/worgarside/home-assistant/commit/7699125c4df4ad2156e2c71f2fc882a5894a4e96))

- 🤖 `prek autoupdate` ([#2844](https://github.com/worgarside/home-assistant/pull/2844),
  [`176dec3`](https://github.com/worgarside/home-assistant/commit/176dec3630db2e96902e791391a5a2a50ad9430e))

### Features

- Add control for Vic's notifications
  ([`e77cef8`](https://github.com/worgarside/home-assistant/commit/e77cef8e286e297b29a3b7ca15f9154f41b4a3e9))

- Handle holiday mode in light alerts
  ([#2847](https://github.com/worgarside/home-assistant/pull/2847),
  [`4316249`](https://github.com/worgarside/home-assistant/commit/431624938c6f9a0f13922d976af79a41da72d803))

- Simplify disk usage notification automation
  ([#2849](https://github.com/worgarside/home-assistant/pull/2849),
  [`6cfdf3a`](https://github.com/worgarside/home-assistant/commit/6cfdf3a83b9f20be206c824e9581eff7943d72b3))

- **automation**: Add alert system for VaultPi storage and pi_stats failures
  ([#2828](https://github.com/worgarside/home-assistant/pull/2828),
  [`c2e0d05`](https://github.com/worgarside/home-assistant/commit/c2e0d05e3072fd2260f4655aedc11b5706afd76e))

- **automation**: Add holiday mode activation via notification
  ([#2839](https://github.com/worgarside/home-assistant/pull/2839),
  [`8a3373e`](https://github.com/worgarside/home-assistant/commit/8a3373e44422329da40eb9d3d67d228001a07bef))

- **threshold**: Add qBittorrent storage cleanup threshold
  ([#2850](https://github.com/worgarside/home-assistant/pull/2850),
  [`3fa77c4`](https://github.com/worgarside/home-assistant/commit/3fa77c4e1b8ac254e83db78b57dcc61e44bfa438))


## v3.31.0 (2026-08-07)

### Bug Fixes

- Correct sensor name typo in office desk config
  ([#2711](https://github.com/worgarside/home-assistant/pull/2711),
  [`86cc0bb`](https://github.com/worgarside/home-assistant/commit/86cc0bb1fcf707ebfd565cd9d30608bfc2f74bd9))

- Don't send error images in notifs
  ([#2812](https://github.com/worgarside/home-assistant/pull/2812),
  [`3ddb0a0`](https://github.com/worgarside/home-assistant/commit/3ddb0a06371ecc5fde1f01fdc74ada8abcbcb93c))

- Handle YAML attributes more robustly
  ([#2792](https://github.com/worgarside/home-assistant/pull/2792),
  [`9fb02de`](https://github.com/worgarside/home-assistant/commit/9fb02de77e2972ec1ddcff741b0b9ded7ddb16da))

- Prepend base URL to notification links
  ([#2811](https://github.com/worgarside/home-assistant/pull/2811),
  [`a245da8`](https://github.com/worgarside/home-assistant/commit/a245da80336456278daa6a66f1490623b728bbe2))

- **automation**: Correct event data key from 'action' to 'service'
  ([#2787](https://github.com/worgarside/home-assistant/pull/2787),
  [`b1725d7`](https://github.com/worgarside/home-assistant/commit/b1725d78bed89451a33b96612403bbacff578bfa))

- **automation**: Ensure charging hub turns off only after timeout
  ([#2717](https://github.com/worgarside/home-assistant/pull/2717),
  [`3b8b2af`](https://github.com/worgarside/home-assistant/commit/3b8b2af66750a9e719ad69ad26621c92fd78f128))

- **camera**: Adjust notification logic for improved filtering
  ([#2813](https://github.com/worgarside/home-assistant/pull/2813),
  [`864b96d`](https://github.com/worgarside/home-assistant/commit/864b96de5857d62b7f4d48be7e66a65a6f79a2fb))

- **notifications**: Ensure front door detection recognizes people accurately
  ([`2f53ca8`](https://github.com/worgarside/home-assistant/commit/2f53ca8945165149341d315b1dda6ff636e4b211))

### Chores

- Habit cleanup ([#2762](https://github.com/worgarside/home-assistant/pull/2762),
  [`ec0b619`](https://github.com/worgarside/home-assistant/commit/ec0b6198a86bd12331ec14fc915e00b8e549ba78))

- Remove aionanoleaf integration
  ([`6437835`](https://github.com/worgarside/home-assistant/commit/6437835d6a3c11abb4556ada8244b653c5ae510e))

- Remove mood tracking entities for Vic and Will
  ([#2766](https://github.com/worgarside/home-assistant/pull/2766),
  [`14bd6cf`](https://github.com/worgarside/home-assistant/commit/14bd6cfbff1bf67010517c2c33a9daad99e160c0))

- Remove MQTT sensors for MtrxPi
  ([`660cc58`](https://github.com/worgarside/home-assistant/commit/660cc588cda7eefafe8a13eb279c5e2f825dd9c6))

- **deps**: Bump cryptography from 48.0.1 to 50.0.0
  ([#2798](https://github.com/worgarside/home-assistant/pull/2798),
  [`31b9be6`](https://github.com/worgarside/home-assistant/commit/31b9be63f481165f0d3e69e70f7fdbd6ff44157d))

- **tooling**: Standardize repo tooling and update workflows
  ([#2814](https://github.com/worgarside/home-assistant/pull/2814),
  [`f18cf51`](https://github.com/worgarside/home-assistant/commit/f18cf51c150be3791e01abda4ba07a121ea1f385))

### Continuous Integration

- **workflows**: Switch to using dev token for semantic release
  ([`fdc732b`](https://github.com/worgarside/home-assistant/commit/fdc732b0f71b7b5aa57c9315926c7e94b52a9d9e))

- **workflows**: Update semantic release authentication method
  ([`59be9af`](https://github.com/worgarside/home-assistant/commit/59be9afbc04c3dcb44c306770353a7241da48157))

### Features

- Add basement presence detection ([#2759](https://github.com/worgarside/home-assistant/pull/2759),
  [`506f246`](https://github.com/worgarside/home-assistant/commit/506f246b1940e5ac7215cf2e2ae5c8679d205603))

- Add Bayesian presence sensors for rooms
  ([#2791](https://github.com/worgarside/home-assistant/pull/2791),
  [`7dccbac`](https://github.com/worgarside/home-assistant/commit/7dccbac1ee99392bf0c48e323337a90ed6eeab2d))

- Add charging hub auto-off notifications
  ([#2794](https://github.com/worgarside/home-assistant/pull/2794),
  [`b4bba80`](https://github.com/worgarside/home-assistant/commit/b4bba80ccbd6e293106c3f2e44336aa09b7dede8))

- Add configurable ceiling for quiet mode
  ([#2730](https://github.com/worgarside/home-assistant/pull/2730),
  [`104b832`](https://github.com/worgarside/home-assistant/commit/104b832e2d94e2ad762a71f3ed1485201e16c7c7))

- Add Monzo reauth variables ([#2763](https://github.com/worgarside/home-assistant/pull/2763),
  [`1efec1d`](https://github.com/worgarside/home-assistant/commit/1efec1dac9eae8b42224c16f63937a2aae37c9b1))

- Add quiet mode source for air purifier
  ([#2708](https://github.com/worgarside/home-assistant/pull/2708),
  [`622b284`](https://github.com/worgarside/home-assistant/commit/622b2844b1d48945ea3ffb2f25faf4c86da4c381))

- Add TrueLayer reauth entities ([#2726](https://github.com/worgarside/home-assistant/pull/2726),
  [`8ecda5f`](https://github.com/worgarside/home-assistant/commit/8ecda5fad682d62cce28ba862d4694cc4a7e1415))

- AI notifications from Frigate ([#2764](https://github.com/worgarside/home-assistant/pull/2764),
  [`1c2e489`](https://github.com/worgarside/home-assistant/commit/1c2e489b6d2059cffb5c62c57710f3e29bd3cbf6))

- Automate AC off timer management ([#2706](https://github.com/worgarside/home-assistant/pull/2706),
  [`2709d7d`](https://github.com/worgarside/home-assistant/commit/2709d7dad52f9f611e1f56edd92a162e881c56e7))

- Cut over OAuth reauth to brokered buttons and vars
  ([#2790](https://github.com/worgarside/home-assistant/pull/2790),
  [`7704e56`](https://github.com/worgarside/home-assistant/commit/7704e56df8b64f9c321a6884aa1a2c7b84cacf9e))

- Enhance OVO usage tracking ([#2712](https://github.com/worgarside/home-assistant/pull/2712),
  [`ba963df`](https://github.com/worgarside/home-assistant/commit/ba963dfeebcc8bc5740682839bd548f03e60a39c))

- Integrate multi-user notifications
  ([#2801](https://github.com/worgarside/home-assistant/pull/2801),
  [`1210493`](https://github.com/worgarside/home-assistant/commit/12104934cdfcad394a599f2624e1205d2608596c))

- Remove visitor mode restrictions ([#2810](https://github.com/worgarside/home-assistant/pull/2810),
  [`8713ccd`](https://github.com/worgarside/home-assistant/commit/8713ccd256e165512def1c0a31d0a4df5b41d284))

- Update add-on sensors ([#2729](https://github.com/worgarside/home-assistant/pull/2729),
  [`0d4ad04`](https://github.com/worgarside/home-assistant/commit/0d4ad040f81d0358b0ee9a45182d74bdd992edd5))

- Visitor mode toggle ([#2800](https://github.com/worgarside/home-assistant/pull/2800),
  [`1233cb2`](https://github.com/worgarside/home-assistant/commit/1233cb2298caabbbc44a806e989a252c069c6e72))

- **appdaemon**: Add TrueLayer auth token and balance entities
  ([#2719](https://github.com/worgarside/home-assistant/pull/2719),
  [`9410164`](https://github.com/worgarside/home-assistant/commit/9410164c5eb47c4df44dacb224f240a1ce0558ba))

- **cursor**: Add sensors and webhook for cursor usage tracking
  ([#2760](https://github.com/worgarside/home-assistant/pull/2760),
  [`fac0aa8`](https://github.com/worgarside/home-assistant/commit/fac0aa89840c92474e4a5b318027195521a78a9d))

- **sensor**: Add average home temperature and humidity sensors
  ([#2720](https://github.com/worgarside/home-assistant/pull/2720),
  [`a88bf05`](https://github.com/worgarside/home-assistant/commit/a88bf05b6712e07ee11b63d854ceef12bfa60c5f))


## v3.30.0 (2026-06-26)

### Bug Fixes

- Address motion sensor unavailable state
  ([#2695](https://github.com/worgarside/home-assistant/pull/2695),
  [`352211e`](https://github.com/worgarside/home-assistant/commit/352211e7c4211d508850d5f94ca49dd642c8033d))

- Correct typo in sensor state condition
  ([`f7935b7`](https://github.com/worgarside/home-assistant/commit/f7935b7b30d265b894febdf30eb12fad0e51cbef))

- Handle missing action in dynamic scripts
  ([#2682](https://github.com/worgarside/home-assistant/pull/2682),
  [`8b61447`](https://github.com/worgarside/home-assistant/commit/8b614477054cdaab1072f130b1bf28bc3b475c67))


## v3.29.0 (2026-05-23)

### Continuous Integration

- Trigger auto-create PR workflow on any non-main branch push
  ([#2670](https://github.com/worgarside/home-assistant/pull/2670),
  [`8f99454`](https://github.com/worgarside/home-assistant/commit/8f994547ce6f383552264c537fafb2742996df9e))

### Refactoring

- Separate UV logic from direct sun detection to streamline code
  ([#2677](https://github.com/worgarside/home-assistant/pull/2677),
  [`abb2491`](https://github.com/worgarside/home-assistant/commit/abb2491b3844b8c49c2b2f77e22d34ddd77bd8fd))


## v3.28.0 (2026-05-09)

### Features

- Allow configuration of dining area big light brightness
  ([#2629](https://github.com/worgarside/home-assistant/pull/2629),
  [`9f33760`](https://github.com/worgarside/home-assistant/commit/9f33760e85a45c32523213cf94dd6df7ed45fd57))


## v3.27.0 (2026-04-14)


## v3.26.0 (2026-04-12)


## v3.25.0 (2026-04-05)


## v3.24.0 (2026-03-28)


## v3.23.0 (2026-02-26)


## v3.22.0 (2026-01-31)


## v3.21.0 (2026-01-17)


## v3.20.0 (2026-01-11)


## v3.19.1 (2026-01-07)


## v3.19.0 (2026-01-05)

### Bug Fixes

- Only trigger air purification if fans not heating
  ([#2452](https://github.com/worgarside/home-assistant/pull/2452),
  [`384df12`](https://github.com/worgarside/home-assistant/commit/384df12a24ae7e90333bdee63452e169d0f4f16e))


## v3.18.0 (2025-12-08)


## v3.17.0 (2025-11-28)

### Bug Fixes

- Debounce central heating off trigger
  ([#2405](https://github.com/worgarside/home-assistant/pull/2405),
  [`78ead14`](https://github.com/worgarside/home-assistant/commit/78ead14ff8330207ddfc10adf74190de58cfa7ce))


## v3.16.0 (2025-10-30)


## v3.15.0 (2025-10-23)


## v3.14.0 (2025-10-19)


## v3.13.1 (2025-10-19)


## v3.13.0 (2025-10-18)


## v3.12.0 (2025-10-12)


## v3.11.0 (2025-10-11)


## v3.10.0 (2025-10-05)


## v3.9.0 (2025-09-30)


## v3.8.0 (2025-08-24)


## v3.7.1 (2025-08-23)


## v3.7.0 (2025-08-20)


## v3.6.0 (2025-08-19)


## v3.5.0 (2025-08-18)


## v3.4.0 (2025-08-10)


## v3.3.0 (2025-08-07)


## v3.2.0 (2025-07-30)


## v3.1.0 (2025-07-27)


## v3.0.0 (2025-07-15)


## v2.103.0 (2025-03-16)


## v2.102.1 (2025-03-11)


## v2.102.0 (2025-03-03)


## v2.101.0 (2025-02-17)


## v2.100.1 (2025-01-13)


## v2.100.0 (2025-01-09)


## v2.99.0 (2025-01-08)


## v2.98.3 (2024-12-29)


## v2.98.2 (2024-12-28)


## v2.98.1 (2024-12-16)


## v2.98.0 (2024-12-07)


## v2.97.0 (2024-12-01)


## v2.96.2 (2024-11-19)


## v2.96.1 (2024-11-17)


## v2.96.0 (2024-11-13)


## v2.95.0 (2024-11-13)


## v2.94.0 (2024-11-12)


## v2.93.0 (2024-11-07)


## v2.92.0 (2024-11-06)


## v2.91.2 (2024-10-29)


## v2.91.1 (2024-10-29)


## v2.91.0 (2024-10-20)


## v2.90.0 (2024-10-07)


## v2.89.1 (2024-10-03)


## v2.89.0 (2024-09-29)


## v2.88.1 (2024-09-28)


## v2.88.0 (2024-09-28)


## v2.87.0 (2024-09-28)


## v2.86.0 (2024-09-27)


## v2.85.2 (2024-09-27)


## v2.85.1 (2024-09-26)


## v2.85.0 (2024-09-15)


## v2.84.1 (2024-09-02)


## v2.84.0 (2024-09-02)


## v2.83.0 (2024-09-01)


## v2.82.0 (2024-08-31)


## v2.81.0 (2024-08-29)


## v2.80.1 (2024-08-29)


## v2.80.0 (2024-08-29)


## v2.79.0 (2024-08-25)


## v2.78.2 (2024-08-19)


## v2.78.1 (2024-08-09)


## v2.78.0 (2024-08-08)


## v2.77.0 (2024-08-04)


## v2.76.1 (2024-08-03)


## v2.76.0 (2024-07-30)


## v2.75.0 (2024-07-22)


## v2.74.0 (2024-07-17)


## v2.73.0 (2024-07-14)


## v2.72.0 (2024-07-10)


## v2.71.0 (2024-07-09)


## v2.70.0 (2024-07-09)


## v2.69.0 (2024-07-07)


## v2.68.0 (2024-07-01)


## v2.67.0 (2024-06-30)


## v2.66.0 (2024-06-28)


## v2.65.0 (2024-06-28)


## v2.64.0 (2024-06-27)


## v2.63.0 (2024-06-26)


## v2.62.0 (2024-06-26)


## v2.61.1 (2024-06-26)


## v2.61.0 (2024-06-25)


## v2.60.0 (2024-06-25)


## v2.59.0 (2024-06-25)


## v2.58.0 (2024-06-25)


## v2.57.0 (2024-06-22)


## v2.56.0 (2024-06-22)


## v2.55.0 (2024-06-18)


## v2.54.0 (2024-06-17)


## v2.53.2 (2024-06-12)


## v2.53.1 (2024-06-10)


## v2.53.0 (2024-06-01)


## v2.52.1 (2024-05-31)


## v2.52.0 (2024-05-27)


## v2.51.0 (2024-05-26)


## v2.50.0 (2024-05-25)


## v2.49.1 (2024-05-24)


## v2.49.0 (2024-05-23)


## v2.48.2 (2024-05-18)


## v2.48.1 (2024-05-18)


## v2.48.0 (2024-05-18)


## v2.47.0 (2024-05-17)


## v2.46.0 (2024-05-16)


## v2.45.1 (2024-05-12)


## v2.45.0 (2024-05-11)


## v2.44.1 (2024-05-11)


## v2.44.0 (2024-05-11)


## v2.43.2 (2024-04-27)


## v2.43.1 (2024-04-27)


## v2.43.0 (2024-04-27)


## v2.42.0 (2024-04-25)


## v2.41.0 (2024-04-19)


## v2.40.0 (2024-04-14)


## v2.39.0 (2024-04-13)


## v2.38.0 (2024-04-13)


## v2.37.1 (2024-03-14)


## v2.37.0 (2024-03-14)


## v2.36.0 (2024-03-13)


## v2.35.4 (2024-03-03)


## v2.35.3 (2024-02-27)


## v2.35.2 (2024-01-24)


## v2.35.1 (2024-01-21)


## v2.35.0 (2024-01-21)


## v2.34.1 (2024-01-21)


## v2.34.0 (2024-01-20)


## v2.33.0 (2024-01-20)


## v2.32.1 (2024-01-19)


## v2.32.0 (2024-01-19)


## v2.31.0 (2024-01-14)


## v2.30.3 (2024-01-11)


## v2.30.2 (2024-01-10)


## v2.30.1 (2024-01-10)


## v2.30.0 (2024-01-10)


## v2.29.0 (2024-01-07)


## v2.28.1 (2024-01-06)


## v2.28.0 (2024-01-06)


## v2.27.3 (2024-01-05)


## v2.27.2 (2024-01-05)


## v2.27.1 (2024-01-03)


## v2.27.0 (2024-01-03)


## v2.26.1 (2024-01-01)


## v2.26.0 (2024-01-01)


## v2.25.0 (2023-12-22)


## v2.24.1 (2023-12-21)


## v2.24.0 (2023-12-21)


## v2.23.3 (2023-12-20)


## v2.23.2 (2023-12-19)


## v2.23.1 (2023-12-19)


## v2.23.0 (2023-12-19)


## v2.22.4 (2023-12-17)


## v2.22.3 (2023-12-16)


## v2.22.2 (2023-12-16)


## v2.22.1 (2023-12-16)


## v2.22.0 (2023-12-15)


## v2.21.0 (2023-12-14)


## v2.20.0 (2023-12-13)


## v2.19.2 (2023-12-13)


## v2.19.1 (2023-12-12)


## v2.19.0 (2023-12-10)


## v2.18.2 (2023-12-09)


## v2.18.1 (2023-12-07)


## v2.18.0 (2023-12-07)


## v2.17.11 (2023-12-06)


## v2.17.10 (2023-12-06)


## v2.17.9 (2023-12-06)


## v2.17.8 (2023-12-06)


## v2.17.7 (2023-12-04)


## v2.17.6 (2023-12-03)


## v2.17.5 (2023-12-03)


## v2.17.4 (2023-12-03)


## v2.17.3 (2023-12-03)


## v2.17.2 (2023-12-02)


## v2.17.1 (2023-12-02)


## v2.17.0 (2023-12-01)


## v2.16.6 (2023-11-29)


## v2.16.5 (2023-11-29)


## v2.16.4 (2023-11-28)


## v2.16.3 (2023-11-28)


## v2.16.2 (2023-11-26)


## v2.16.1 (2023-11-26)


## v2.16.0 (2023-11-26)


## v2.15.1 (2023-11-25)


## v2.15.0 (2023-11-25)


## v2.14.3 (2023-11-24)


## v2.14.2 (2023-11-24)


## v2.14.1 (2023-11-24)


## v2.14.0 (2023-11-24)


## v2.13.0 (2023-11-23)


## v2.12.0 (2023-11-19)


## v2.11.3 (2023-11-16)


## v2.11.2 (2023-11-15)


## v2.11.1 (2023-11-15)


## v2.11.0 (2023-11-12)


## v2.10.0 (2023-11-11)


## v2.9.3 (2023-11-10)


## v2.9.2 (2023-11-05)


## v2.9.1 (2023-11-05)


## v2.9.0 (2023-11-05)


## v2.8.2 (2023-11-05)


## v2.8.1 (2023-11-05)


## v2.8.0 (2023-11-05)


## v2.7.1 (2023-11-02)


## v2.7.0 (2023-11-01)


## v2.6.0 (2023-10-29)


## v2.5.1 (2023-10-29)


## v2.5.0 (2023-10-29)


## v2.4.0 (2023-10-28)


## v2.3.0 (2023-10-27)


## v2.2.0 (2023-10-26)


## v2.1.0 (2023-10-09)


## v2.0.0 (2023-10-08)


## v1.7.1 (2023-09-21)


## v1.7.0 (2023-09-21)


## v1.6.0 (2023-08-07)


## v1.5.0 (2023-08-02)


## v1.4.0 (2023-07-05)


## v1.3.1 (2023-07-04)


## v1.3.0 (2023-07-02)


## v1.2.0 (2023-06-25)


## v1.1.0 (2023-06-24)


## v1.0.0 (2023-06-24)


## v0.6.1 (2023-05-07)


## v0.6.0 (2023-05-07)


## v0.5.0 (2023-05-07)


## v0.4.0 (2023-05-02)


## v0.3.0 (2023-04-23)


## v0.2.1 (2023-04-23)


## v0.2.0 (2023-04-22)


## v0.1.0 (2023-04-20)

- Initial Release
