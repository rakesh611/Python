# as
# Creates an alias.
# Very common with imports.
import subprocess as sp

result = sp.run(["hostname"], capture_output=True, text=True)

print(result.stdout)