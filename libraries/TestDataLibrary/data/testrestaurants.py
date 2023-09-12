

"""
tags = used to identify which restaurant is needed.

NOTES!!! 
All test restaurants should be tagged by their type:
- external
- pos_and_oo
- pos_only
- oo_only

Tags must not have spaces and must be in lower case.
"""

from libraries.TestDataLibrary.dto.testrestodetails import TestRestaurantDetails


QA_TEST_RESTAURANTS: list[dict] = [
    {
        "tags": ["external", "printer_editor1"],
        "details": TestRestaurantDetails(
            rid="c0dfee77-ce1c-4e6b-86d5-5da1044abf0c",
            ex_name="R900144",
            en_name="ZZINVOICE 00144",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0144"
        )
    },
    {
        "tags": ["pos_and_oo", "printer_editor2"],
        "details": TestRestaurantDetails(
            rid="77848751-8d10-439b-be70-3ce4e9f0d534",
            ex_name="R900001",
            en_name="ZZINVOICE 00001",
            address1="418 Dundas St W",
            address2="",
            city="Toronto",
            state="ON",
            zipcode="M5T 1G2",
            contact_phone1="1111-100-0001"
        )
    },
    {
        "tags": ["pos_only", "printer_edito3", "order-receipt-2.0.ftl"],
        "details": TestRestaurantDetails(
            rid="a4c019af-e994-4c3a-8a4a-e8c8af2341e9",
            ex_name="R900143",
            en_name="ZZINVOICE 00143",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0143"
        )
    },
    {
        "tags": ["oo_only", "printer_editor4"],
        "details": TestRestaurantDetails(
            rid="bd5a117f-4e91-4a19-a4de-f43efc9126cc",
            ex_name="R900142",
            en_name="ZZINVOICE 00142",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0142"
        )
    },
    {
        "tags": ["external", "order-receipt-2.0.ftl", "english-only-order-receipt-2.0-large-font.ftl", "order-receipt-2.0-large-en-font.ftl"],
        "details": TestRestaurantDetails(
            rid="4da33250-0f91-420c-9220-7ad8f81d6cfd",
            ex_name="R900101",
            en_name="ZZINVOICE 00101",
            address1="5301 Belair Rd",
            address2="1215",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0101"
        )
    },
    {
        "tags": ["pos_and_oo", "order-receipt-2.0.ftl", "english-only-order-receipt-2.0-large-font.ftl","order-receipt-2.0-large-en-font.ftl"],
        "details": TestRestaurantDetails(
            rid="71d1eab7-35eb-409e-9f1f-3468c3e35f60",
            ex_name="R900111",
            en_name="ZZINVOICE 00111",
            address1="2315 Logan Ave",
            address2="1215",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0111"
        )
    },
    {
        "tags": ["external", "english-only-order-receipt-2.0-larger-font.ftl","order-receipt-2.0-large-bold-ch-font.ftl"],
        "details": TestRestaurantDetails(
            rid="9c0d5ad4-fc45-45fd-a517-a5b563659060",
            ex_name="R900121",
            en_name="ZZINVOICE 00121",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0121"
        )
    },
    {
        "tags": ["pos_and_oo", "english-only-order-receipt-2.0-larger-font.ftl", 
                 "chinese-only-order-receipt-2.0-large-font.ftl", "order-receipt-2.0-large-ch-font.ftl",
                 "order-receipt-2.0-large-bold-ch-font.ftl"],
        "details": TestRestaurantDetails(
            rid="f08f3c71-d444-4204-aee8-b602d0b906fc",
            ex_name="R900122",
            en_name="ZZINVOICE 00122",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0122"
        )
    },
    {
        "tags": ["external", "dynamic-order-receipt-no-totals.ftl", "chinese-only-order-receipt-2.0-large-font.ftl"],
        "details": TestRestaurantDetails(
            rid="5ff2dd47-01a7-4adf-9b5d-d204c59e720e",
            ex_name="R900012",
            en_name="ZZINVOICE 00012",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0012"
        )
    },
    {
        "tags": ["pos_and_oo", "dynamic-order-receipt-no-totals.ftl", "dynamic-kitchen-order-receipt.ftl", "dynamic-order-receipt.ftl"],
        "details": TestRestaurantDetails(
            rid="6ecbdd35-6464-4ec0-90e5-31a18a5b7eb5",
            ex_name="R900022",
            en_name="ZZINVOICE 00022",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0022"
        )
    },
    {
        "tags": ["external", "dynamic-kitchen-order-receipt.ftl", "order-receipt-2.0-large-ch-font.ftl"],
        "details": TestRestaurantDetails(
            rid="732e0c57-90f3-4a13-b312-414b5b336444",
            ex_name="R900021",
            en_name="ZZINVOICE 00021",
            address1="5301 Belair Rd",
            address2="15",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0021"
        )
    },

    {
        "tags": ["external", "dynamic-order-receipt.ftl"],
        "details": TestRestaurantDetails(
            rid="05f02738-62da-4666-802a-175571bb3f2c",
            ex_name="R900017",
            en_name="ZZINVOICE 00017",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0017"
        )
    },
    {
        "tags": ["suspended", "ctd"],
        "details": TestRestaurantDetails(
            rid="527960fa-6e19-4491-b8ab-3b093afcbbc1",
            ex_name="R900190",
            en_name="ZZINVOICE 00190",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0190"
        )
    },
    {
        "tags": ["open", "ctd"],
        "details": TestRestaurantDetails(
            rid="7b7a6e96-54c2-493b-ac9f-6fcaead234da",
            ex_name="R900191",
            en_name="ZZINVOICE 00191",
            address1="2315 Logan Ave",
            address2="",
            city="Waterloo",
            state="IA",
            zipcode="50703",
            contact_phone1="100-000-0191"
        )
    },
    {
        "tags": ["america/new_york"],
        "details": TestRestaurantDetails(
            rid="224688c7-1d7c-45d5-b07f-c644d0adcecc",
            ex_name="R900010",
            en_name="ZZINVOICE 00010",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0010"
        )
    },
    {
        "tags": ["america/chicago"],
        "details": TestRestaurantDetails(
            rid="62d246db-474c-4160-8948-bee74ded5cef",
            ex_name="R900011",
            en_name="ZZINVOICE 00011",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0011"
        )
    },
    {
        "tags": ["america/denver"],
        "details": TestRestaurantDetails(
            rid="2829021c-7aa3-4dd9-9aba-88b88fa03cce",
            ex_name="R900025",
            en_name="ZZINVOICE 00025",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0025"
        )
    },
      {
        "tags": ["america/los_angeles"],
        "details": TestRestaurantDetails(
            rid="469d6242-13da-4f4b-b3de-460d9cc40ff0",
            ex_name="R900040",
            en_name="ZZINVOICE 00040",
            address1="5301 Belair Rd",
            address2="",
            city="Baltimore",
            state="MD",
            zipcode="21206",
            contact_phone1="100-000-0040"
        )
    },
]


PROD_TEST_RESTAURANTS: list[dict] = [
    {
        "tags": ["chef_kwo_skt"],
        "details": TestRestaurantDetails(
            rid="b544ae46-5dce-477f-a46d-2ac34175622f",
            ex_name="R987652",
            en_name="CHEF KWO SKT",
            address1="15105-G John J. Delaney DR.",
            address2="",
            city="Charlotte",
            state="NC",
            zipcode="28277",
            contact_phone1="(845) 709-5420-123456"
        )
    },
    {
        "tags": ["ambers_garden"],
        "details": TestRestaurantDetails(
            rid="35b5541b-7203-4824-b2d4-9eeaab7f466f",
            ex_name="R987653",
            en_name="AMBER'S GARDEN",
            address1="396-398 Broad St",
            address2="",
            city="Bloomfield",
            state="NJ",
            zipcode="07003",
            contact_phone1="1175416313"
        )
    },
    {
        "tags": ["sakan_bento"],
        "details": TestRestaurantDetails(
            rid="250379c1-9dff-11e5-8ff4-80ee733c5b56",
            ex_name="R88266",
            en_name="SAKAN BENTO",
            address1="606 N Wellwood Ave",
            address2="",
            city="Lindenhurst",
            state="NY",
            zipcode="11757",
            contact_phone1="(131)226-6800/6818"
        )
    },
    {
        "tags": ["skt_demo_restaurant"],
        "details": TestRestaurantDetails(
            rid="3f00ecca-6645-4cce-95e7-33b697abbeba",
            ex_name="R987651",
            en_name="SKT DEMO RESTAURANT",
            address1="33-01 Queens Blvd",
            address2="",
            city="Queens",
            state="NY",
            zipcode="11101",
            contact_phone1="(845) 709-5431"
        )
    }
]