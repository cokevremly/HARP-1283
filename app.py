import streamlit as st

from analyzer import analyze_url
from scorer import calculate_score, get_risk_level
from whois_lookup import get_whois_info
from ssl_lookup import get_ssl_info
from dns_lookup import dns_lookup
from virustotal_lookup import virustotal_lookup
from abuseipdb_lookup import check_ip
from otx_lookup import check_ip_otx


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="HARP-1283 \n Hybrid Analysis & Reconnaissance Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    /* General text */
    .stApp p,
    .stApp label,
    .stApp span {
        color: #ffffff;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #ffffff;
    }

    .subtitle {
        color: #ffffff;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Cards */
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 1.3rem;
        text-align: center;
    }

    .metric-title {
        color: #ffffff;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }

    .metric-value {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 700;
    }

    /* Section titles */
    .section-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    /* Findings */
    .finding {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #ffffff;
        font-size: 0.8rem;
        margin-top: 3rem;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🛡️ HARP-1283</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Hybrid Analysis & Reconnaissance Platform'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# URL INPUT
# --------------------------------------------------

col_input, col_button = st.columns([5, 1])

with col_input:

    url = st.text_input(
        "Target URL",
        placeholder="https://example.com",
        label_visibility="collapsed"
    )

with col_button:

    analyze_button = st.button(
        "Analyze",
        type="primary",
        use_container_width=True
    )


# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if analyze_button:

    if not url:
        st.warning("Please enter a URL.")
        st.stop()

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    with st.spinner("Analyzing target..."):

        # URL analysis
        findings = analyze_url(url)

        # WHOIS
        whois_info = get_whois_info(url)

        # SSL
        ssl_info = get_ssl_info(url)

        # DNS
        dns_info = dns_lookup(url)

        # Get IP address
        ip = dns_info["A"][0] if dns_info.get("A") else None

        # Threat intelligence
        abuseipdb_info = check_ip(ip)
        otx_info = check_ip_otx(ip)
        virustotal_info = virustotal_lookup(url)

        # Calculate score
        score = calculate_score(
            findings,
            virustotal_info,
            abuseipdb_info,
            otx_info
        )

        risk_level = get_risk_level(score)


    # --------------------------------------------------
    # TARGET
    # --------------------------------------------------

    st.caption("Analyzed Target")

    st.code(
        url,
        language="text"
    )

    st.divider()


    # --------------------------------------------------
    # RISK SUMMARY
    # --------------------------------------------------

    score_col, level_col = st.columns(2)

    with score_col:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Risk Score</div>
                <div class="metric-value">{score}/100</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with level_col:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Risk Level</div>
                <div class="metric-value">{risk_level}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------
    # SECURITY FINDINGS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">Security Findings</div>',
        unsafe_allow_html=True
    )

    if findings:

        for finding in findings:

            if "detected" in finding.lower():

                st.markdown(
                    f"""
                    <div class="finding">
                        ⚠️ {finding}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="finding">
                        ✓ {finding}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:

        st.success(
            "No security findings detected."
        )


    # --------------------------------------------------
    # SSL + DNS
    # --------------------------------------------------

    ssl_col, dns_col = st.columns(2)


    # --------------------------------------------------
    # SSL INFORMATION
    # --------------------------------------------------

    with ssl_col:

        st.markdown(
            '<div class="section-title">SSL / TLS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"**Issuer:** "
            f"{ssl_info.get('issuer', 'Unknown')}"
        )

        st.markdown(
            f"**Issued To:** "
            f"{ssl_info.get('issued_to', 'Unknown')}"
        )

        st.markdown(
            f"**Valid Until:** "
            f"{ssl_info.get('valid_until', 'Unknown')}"
        )

        st.markdown(
            f"**Days Remaining:** "
            f"{ssl_info.get('days_remaining', 'Unknown')}"
        )


    # --------------------------------------------------
    # DNS INFORMATION
    # --------------------------------------------------

    with dns_col:

        st.markdown(
            '<div class="section-title">DNS Information</div>',
            unsafe_allow_html=True
        )

        for record_type in ["A", "AAAA", "MX", "CNAME"]:

            records = dns_info.get(
                record_type,
                []
            )

            if records:

                st.markdown(
                    f"**{record_type}**"
                )

                for record in records:

                    st.write(record)

            else:

                st.markdown(
                    f"**{record_type}:** —"
                )


    # --------------------------------------------------
    # VIRUSTOTAL
    # --------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">VirusTotal</div>',
        unsafe_allow_html=True
    )

    if "error" in virustotal_info:

        st.warning(
            virustotal_info["error"]
        )

    else:

        vt_cols = st.columns(4)

        vt_fields = [
            (
                "Malicious",
                virustotal_info.get(
                    "Malicious",
                    0
                )
            ),
            (
                "Suspicious",
                virustotal_info.get(
                    "Suspicious",
                    0
                )
            ),
            (
                "Harmless",
                virustotal_info.get(
                    "Harmless",
                    0
                )
            ),
            (
                "Undetected",
                virustotal_info.get(
                    "Undetected",
                    0
                )
            )
        ]

        for col, (name, value) in zip(
            vt_cols,
            vt_fields
        ):

            with col:

                st.metric(
                    name,
                    value
                )


    # --------------------------------------------------
    # ABUSEIPDB
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">AbuseIPDB</div>',
        unsafe_allow_html=True
    )

    data = abuseipdb_info.get(
        "data",
        {}
    )

    if data:

        abuse_cols = st.columns(4)

        with abuse_cols[0]:

            st.metric(
                "IP Address",
                data.get(
                    "ipAddress",
                    "Unknown"
                )
            )

        with abuse_cols[1]:

            st.metric(
                "Abuse Score",
                data.get(
                    "abuseConfidenceScore",
                    "Unknown"
                )
            )

        with abuse_cols[2]:

            st.metric(
                "Country",
                data.get(
                    "countryCode",
                    "Unknown"
                )
            )

        with abuse_cols[3]:

            st.metric(
                "Reports",
                data.get(
                    "totalReports",
                    "Unknown"
                )
            )

    else:

        st.info(
            "No AbuseIPDB information available."
        )


    # --------------------------------------------------
    # ALIENVAULT OTX
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">AlienVault OTX</div>',
        unsafe_allow_html=True
    )

    if otx_info:

        otx_cols = st.columns(3)

        with otx_cols[0]:

            st.metric(
                "Reputation",
                otx_info.get(
                    "reputation",
                    "Unknown"
                )
            )

        with otx_cols[1]:

            st.metric(
                "Pulse Count",
                otx_info.get(
                    "pulse_info",
                    {}
                ).get(
                    "count",
                    "Unknown"
                )
            )

        with otx_cols[2]:

            st.metric(
                "Country",
                otx_info.get(
                    "country_name",
                    "Unknown"
                )
            )

    else:

        st.info(
            "No OTX information available."
        )


    # --------------------------------------------------
    # DNS DETAILED RECORDS
    # --------------------------------------------------

    with st.expander(
        "DNS Detailed Records"
    ):

        for record_type, records in dns_info.items():

            st.markdown(
                f"**{record_type}**"
            )

            if records:

                for record in records:

                    st.write(record)

            else:

                st.write(
                    "No records found."
                )


    # --------------------------------------------------
    # WHOIS INFORMATION
    # --------------------------------------------------

    with st.expander(
        "WHOIS Information"
    ):

        whois_fields = {

            "Registrar":
                whois_info.get(
                    "registrar",
                    "Unknown"
                ),

            "Creation Date":
                whois_info.get(
                    "creation_date",
                    "Unknown"
                ),

            "Updated Date":
                whois_info.get(
                    "updated_date",
                    "Unknown"
                ),

            "Expiration Date":
                whois_info.get(
                    "expiration_date",
                    "Unknown"
                ),

            "DNSSEC":
                whois_info.get(
                    "dnssec",
                    "Unknown"
                )
        }

        for name, value in whois_fields.items():

            st.markdown(
                f"**{name}:** {value}"
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        HARP-1283<br>
        Hybrid Analysis & Reconnaissance Platform
    </div>
    """,
    unsafe_allow_html=True
)
