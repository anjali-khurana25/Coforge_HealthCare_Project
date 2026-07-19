test_coverage = float(input("Enter test coverage percentage: "))
security_scan = input("Did the security scan pass? (yes/no): ").lower()
code_review = input("Is the code review completed? (yes/no/pending): ").lower()
environment = input("Enter environment (development/staging/production): ").lower()

if security_scan == "no":
    print("Deployment Status: Rejected")
    print("Reason: Security scan failed.")

elif environment == "production" and test_coverage >= 80 and security_scan == "yes" and code_review == "yes":
    print("Deployment Status: Approved for Production")

elif environment == "staging" and security_scan == "yes":
    print("Deployment Status: Approved with Warning for Staging")

elif environment == "development" and code_review == "pending" and security_scan == "yes":
    print("Deployment Status: Conditionally Approved")

else:
    print("Deployment Status: Rejected")