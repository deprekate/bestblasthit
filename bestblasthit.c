/* 
    bestblasthit
    Copyright (C) 2019 Katelyn McNair
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

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
