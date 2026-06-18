
import streamlit as st

st.title(" Ứng dụng tính Thuế Thu Nhập Cá Nhân")

# Nhập thu nhập chịu thuế
thu_nhap = st.number_input(
    "Nhập thu nhập chịu thuế (triệu đồng/tháng)",
    min_value=0.0,
    value=20.0
)

if st.button("Tính thuế"):

    if thu_nhap <= 5:
        thue = thu_nhap * 0.05

    elif thu_nhap <= 10:
        thue = 5 * 0.05 + (thu_nhap - 5) * 0.10

    elif thu_nhap <= 18:
        thue = 5 * 0.05 + 5 * 0.10 + (thu_nhap - 10) * 0.15

    elif thu_nhap <= 32:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + (thu_nhap - 18) * 0.20
        )

    elif thu_nhap <= 52:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + (thu_nhap - 32) * 0.25
        )

    elif thu_nhap <= 80:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + 20 * 0.25
            + (thu_nhap - 52) * 0.30
        )

    else:
        thue = (
            5 * 0.05
            + 5 * 0.10
            + 8 * 0.15
            + 14 * 0.20
            + 20 * 0.25
            + 28 * 0.30
            + (thu_nhap - 80) * 0.35
        )

    thu_nhap_sau_thue = thu_nhap - thue

    st.success("Kết quả tính toán")

    st.write(f" Thu nhập chịu thuế: **{thu_nhap:,.2f} triệu đồng**")
    st.write(f" Thuế TNCN phải nộp: **{thue:,.2f} triệu đồng**")
    st.write(f" Thu nhập sau thuế: **{thu_nhap_sau_thue:,.2f} triệu đồng**")
