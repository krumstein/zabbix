DELETE FROM regexps WHERE regexpid=1000;
DELETE FROM expressions WHERE expressionid=1000;

INSERT INTO regexps VALUES ( 1000, "Mounts", "");
INSERT INTO expressions VALUES ( 1000, 1000, ".*", 3, ",", 0 );

