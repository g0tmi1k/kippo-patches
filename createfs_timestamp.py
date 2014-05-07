--- ../utils/createfs.py
+++ ../utils/createfs.py
@@ -26,7 +26,7 @@
             continue

         entry = [name, T_FILE, s.st_uid, s.st_gid, s.st_size, s.st_mode, \
-            int(s.st_ctime), [], None, None]
+            int(s.st_mtime), [], None, None]

        if S_ISLNK(s[ST_MODE]):
            entry[A_TYPE] = T_LINK
