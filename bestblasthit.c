#include <stdio.h>
#include <string.h>


int main() {
	char buf[BUFSIZ];
	char out[BUFSIZ];
	char last_subject[BUFSIZ];
	char *tok;

	while(fgets(buf, sizeof buf, stdin)){
		if (buf[strlen(buf)-1] == '\n') {
			strcpy(out, buf);
			tok = strtok(buf, "\t");
			if(tok != NULL){
				if(strcmp(last_subject, tok) == 0){
					// already seen a hit for this subject
					continue;
				}else{
					// haven't seen a hit for this subject
					strcpy(last_subject, tok);
					tok = strtok(NULL, "\t");
					if(tok != NULL){
						if(strcmp(last_subject, tok) == 0){
							// subject and hit are the same so rewind
							strcpy(last_subject, "\n");
							continue;
						}else{
							printf("%s", out);
						}
					}
				}
			}
		} else {
		    //truncated
		}
	}
	return 0;
}
