from typing import Dict
from dataclasses import field
from pydantic.dataclasses import dataclass


@dataclass
class CategoricalDataConfig:
    YY11_Country: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "Austria",
            2.0: "Belgium",
            3.0: "Bulgaria",
            4.0: "Cyprus",
            5.0: "Czech Republic",
            6.0: "Germany",
            7.0: "Denmark",
            8.0: "Estonia",
            9.0: "Greece",
            10.0: "Spain",
            11.0: "Finland",
            12.0: "France",
            13.0: "Hungary",
            14.0: "Ireland",
            15.0: "Italy",
            16.0: "Lithuania",
            17.0: "Luxembourg",
            18.0: "Latvia",
            19.0: "Malta",
            20.0: "Netherland",
            21.0: "Poland",
            22.0: "Portugal",
            23.0: "Romania",
            24.0: "Sweden",
            25.0: "Slovenia",
            26.0: "Slovakia",
            27.0: "UK",
            28.0: "Turkey",
            29.0: "Croatia",
            30.0: "Macedonia (FYROM)",
            31.0: "Kosovo",
            32.0: "Serbia",
            33.0: "Montenegro",
            34.0: "Iceland",
            35.0: "Norway",
        }
    )
    Y11_Q31: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "Married or living with partner",
            2.0: "Separated or divorced and not living with partner",
            3.0: "Widowed and not living with partner",
            4.0: "Never married and not living with partner",
        }
    )

    Y11_ISCEDsimple: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "No education completed (ISCED 0)",
            2.0: "Primary education (ISCED 1)",
            3.0: "Lower secondary education (ISCED 2)",
            4.0: "Upper secondary education (ISCED 3)",
            5.0: "Post-secondary including pre-vocational or vocational education but not tertiary (ISCED 4)",
            6.0: "Tertiary education – first level (ISCED 5)",
            7.0: "Tertiary education – advanced level (ISCED 6)",
            8.0: "Not applicable",
        }
    )

    Y11_Q49: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "The open countryside",
            2.0: "A village/small town",
            3.0: "A medium to large town",
            4.0: "A city or city suburb",
        }
    )
    Y11_Agecategory: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "18-24",
            2.0: "25-34",
            3.0: "35-49",
            4.0: "50-64",
            5.0: "65+",
        }
    )
    Y11_HH2a: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "Male",
            2.0: "Female",
        }
    )
    Y11_HHsize: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "1 person household",
            2.0: "2 person household",
            3.0: "3 person household",
            4.0: "4 or more person household",
        }
    )
    Y11_Q42: Dict[int, str] = field(
        default_factory=lambda: {
            1.0: "Very good",
            2.0: "Good",
            3.0: "Fair",
            4.0: "Bad",
            5.0: "Very bad",
        }
    )