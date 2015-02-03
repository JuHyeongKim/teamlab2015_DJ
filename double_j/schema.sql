CREATE TABLE `Comment` (
  `CommentID` int(11) NOT NULL,
  `CommentDesc` varchar() NOT NULL,
  `CreateDate` varchar(255) NOT NULL,
  PRIMARY KEY (`CommentID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Posting` (
  `PostingID` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `PostingDesc` varchar(255) NOT NULL,
  `CreatedDate` varchar(255) NOT NULL,
  `View` varchar(255) NOT NULL,
  `TradeOrNot` varchar(45) NOT NULL,
  `Category` varchar(45) NOT NULL,
  PRIMARY KEY (`PostingID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `Message` (
  `MessageID` int(11) NOT NULL,
  `MessageDesc` varchar(255) NOT NULL,
  `SendingDate` varchar(255) NOT NULL,
  PRIMARY KEY (`MessageID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `User` (
  `UserID` varchar(255) NOT NULL,
  `UserNIickname` varchar(255) NOT NULL,
  `UserPassword` varchar(255) NOT NULL,
  `UserEmail` varchar(255) NOT NULL,
  `QuetionForFindingPassword` varchar(255) NOT NULL,
  `AnswerForFindingPassword` varchar(255) NOT NULL,
  PRIMARY KEY (`UserEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
