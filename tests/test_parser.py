from src.core.parser import LogParser

APACHE_LINE = '127.0.0.1 - - [12/Dec/2024:19:06:34 +0000] "GET / HTTP/1.1" 200 612'
AUTH_LINE = 'Dec 12 19:05:08 myhost sshd[1235]: Failed password for invalid user admin from 198.51.100.23 port 51235 ssh2'



def test_apache_parse():
    p = LogParser("apache_common")
    rec = p.parse_line(APACHE_LINE)
    assert rec is not None
    assert rec["ip"] == "127.0.0.1"
    assert rec["status"] == 200
    assert "dt" in rec



def test_auth_parse():
    p = LogParser("auth")
    rec = p.parse_line(AUTH_LINE)
    assert rec is not None
    assert "message" in rec
    assert rec["host"] == "myhost"
    # ensure ip extracted
    assert rec.get("ip") == "198.51.100.23"
