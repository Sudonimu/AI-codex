 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/main.py b/main.py
index ae7fe221b202ef6bfb3b816bd872eeca6be5ba2a..8b46f6f73a7da068894c12bcddc0905ce1ed1cd9 100644
--- a/main.py
+++ b/main.py
@@ -1,8 +1,17 @@
-def greet(name):
+def greet(name: str) -> str:
+    """Return a greeting for the provided name."""
     return f"Hello, {name}!"
 
 def add(a, b):
+    """Return the sum of ``a`` and ``b``.
+
+    Raises:
+        TypeError: If either argument is a string.
+    """
+    if isinstance(a, str) or isinstance(b, str):
+        raise TypeError("add function does not accept string arguments")
     return a + b
 
-print(greet("Codex"))
-print(add(3, 5))
+if __name__ == "__main__":
+    print(greet("Codex"))
+    print(add(3, 5))
 
EOF
)
