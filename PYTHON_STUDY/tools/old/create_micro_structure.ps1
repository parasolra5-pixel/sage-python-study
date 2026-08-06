$folders = @(
    "01_basics\variables",
    "01_basics\input_output",
    "01_basics\comments",

    "02_strings\creation",
    "02_strings\length",
    "02_strings\indexing",
    "02_strings\slicing",
    "02_strings\formatting",

    "03_numbers\integer",
    "03_numbers\float",
    "03_numbers\operators",

    "04_conditions\if",
    "04_conditions\if_else",
    "04_conditions\elif",

    "05_loops\for",
    "05_loops\while",
    "05_loops\range",

    "06_data_structures\list",
    "06_data_structures\tuple",
    "06_data_structures\dictionary",

    "07_functions\basic",
    "07_functions\parameter",
    "07_functions\return",

    "08_modules\import",
    "08_modules\built_in",

    "09_files\text",
    "09_files\json",

    "10_object_oriented\class_basic",

    "11_errors\try_except",

    "12_ai_python\numpy",
    "12_ai_python\pandas",

    "99_ona_system\dictionary",
    "99_ona_system\metadata",
    "99_ona_system\loader"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

Write-Host "완료! ONA 구조 생성됨"


PYTHON_STUDY
└─micro_examples

1단계 ⭐
└─01_basics
   ├─variables
   ├─input_output
   └─comments


2단계
└─02_strings

3단계
└─03_numbers

...

마지막 단계
└─99_ona_system
   ├─dictionary
   ├─loader
   └─metadata