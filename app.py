import dns.resolver
import whois
from prettytable import PrettyTable
import argparse

def nslookup_with_google_dns(domain, query_type=None):
    google_dns_servers = ['8.8.8.8', '8.8.4.4']

    table = PrettyTable()
    table.field_names = ["Record Type", "Result"]

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = google_dns_servers

        query_types = query_type if query_type else ['A', 'NS', 'MX', 'CNAME', 'TXT']

        for q_type in query_types:
            try:
                records = resolver.resolve(domain, q_type)
                for record in records:
                    if q_type == 'TXT':
                        # Decode bytes to UTF-8
                        result_value = record.strings[0].decode('utf-8')
                        table.add_row([q_type, result_value])
                    elif q_type == 'MX':
                        table.add_row([q_type, record.exchange])
                    else:
                        table.add_row([q_type, record.address if q_type == 'A' else record.target])
            except dns.resolver.NoAnswer as e:
                table.add_row([q_type, f"No {q_type} record found for {domain}"])
            except dns.exception.DNSException as e:
                table.add_row([q_type, f"Error: {e}"])

    except Exception as e:
        table.add_row(["General", f"Error: {e}"])

    try:
        # WHOIS bilgileri
        whois_info = whois.whois(domain)
        table.add_row(["WHOIS", str(whois_info.expiration_date)])

    except Exception as e:
        table.add_row(["WHOIS", f"Error: {e}"])

    print(table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform DNS lookup and WHOIS queries for a domain.")
    parser.add_argument("domain", nargs="?", help="Domain name to query")
    parser.add_argument("-t", "--type", nargs="*", choices=['A', 'NS', 'MX', 'CNAME', 'TXT'],
                        help="Specify the record type(s) to query (e.g., A, NS, MX, CNAME, TXT)")
    
    args = parser.parse_args()

    if args.domain:
        domain_name = args.domain
    else:
        domain_name = input("Enter the domain name: ")

    query_types = args.type

    nslookup_with_google_dns(domain_name, query_types)
