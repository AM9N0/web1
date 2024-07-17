const os = require('os');
const crypto = require('crypto');
const https = require("https");
const readline = require("readline");
const {
  exec
} = require("child_process");
console.clear();
console.log("\n[1;36m===============================================\n[1;33m[×] Developed By WASIF MUBEEN QURESHI\n[1;36m===============================================\n[1;31m[•] AUTHOR       : WASIF MUBEEN QURESHI\n[1;33m[•] YOUTUBE      : MR WASIF\n[1;33m[•] Whatsaap     : +923491960523\n[1;33m[•] GITHUB       : W4SIF007\n[1;33m[•] Tool         : Web To Web ConVo\n[1;31m[•] FaceBook     : WASIF MUBEEN QURESHI\n[1;36m===============================================\n[1;33mIF YOU ARE BAD (MERA PUTAR) I AM YOUR DAD\n[1;36m===============================================");
console.log("[1;33m----------------------------------------------");
console.log("[32mImportant Note");
console.log("[1;33m----------------------------------------------");
console.log("[32mWifi + Sim Data Working");
console.log("[1;33mMulti Ids Web To Web Convo");
console.log("[1;33mMulti ids + Multi +group+multi+targets");
console.log("[1;33mMonthly Subscription Price Rs :500");
console.log("[1;33mGod abuser ki aprovle hata di jaigi");
console.log("[32mYour Key is not approved");
console.log("[1;33m----------------------------------------------");
console.log("[32mYou Have to Take Approval first");
console.log("[1;33m----------------------------------------------");
const uniqueKey = crypto.createHash('sha256').update(os.userInfo().uid.toString() + os.userInfo().username).digest('hex');
console.log("[32mYour Key:", uniqueKey);
console.log("[1;33m----------------------------------------------");
checkPermission(uniqueKey);
function getUniqueId() {
  return crypto.createHash('sha256').update(os.userInfo().uid.toString() + os.userInfo().username).digest('hex');
}
function checkPermission(_0x5ccca4) {
  axios.get("https://pastebin.com/raw/SSMZjjGe").then(_0x111dd9 => {
    let _0x4ec99e = _0x111dd9.data;
    let _0x3b9b94 = _0x4ec99e.split("\n").map(_0x301e2a => _0x301e2a.trim()).filter(_0x5f24c4 => _0x5f24c4.includes(_0x5ccca4));
    if (_0x3b9b94.length === 0) {
      console.log("[31mSorry, you don't have permission to run this script.");
      sendApprovalRequest(_0x5ccca4);
    } else {
      console.log("[32mPermission granted. You can proceed with the script.");
      console.clear();
      console.log("\n[1;36m===============================================\n[1;33m[×] Developed By WASIF MUBEEN QURESHI\n[1;36m===============================================\n[1;31m[•] AUTHOR       : WASIF MUBEEN QURESHI\n[1;33m[•] YOUTUBE      : MR WASIF\n[1;33m[•] Whatsaap     : +923491960523\n[1;33m[•] GITHUB       : W4SIF007\n[1;33m[•] Tool         : Web To Web ConVo\n[1;31m[•] FaceBook     : WASIF MUBEEN QURESHI\n[1;36m===============================================\n[1;33mIF YOU ARE BAD (MERA PUTAR) I AM YOUR DAD\n[1;36m===============================================");
      console.log("[33m%s[0m", '');
      const _0x177d0f = require("prompt");
      const _0x4d7ed4 = require('fs');
      const _0x442e23 = require("fca-unofficial");
      const _0x423fa1 = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"];
      const _0x242c6a = new https.Agent({
        'rejectUnauthorized': false
      });
      _0x177d0f.start();
      _0x177d0f.get(["IdNAME", "IdNAME2", "IdNAME3", "IdNAME4", 'IdNAME5', 'IdNAME6', "IdNAME7", 'IdNAME8'], function (_0x290577, _0xbf8432) {
        if (_0x290577) {
          return _0x4f8ee7(_0x290577);
        }
        _0x40eb9f('', _0xbf8432);
      });
      function _0x40eb9f(_0x3f0e4f, _0xd352df) {
        let _0x328557 = [JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME2 || '' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME3 || '' + _0xd352df.IdNAME, "utf8")), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME4 || '' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME5 || '' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME6 || '' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME7 || '' + _0xd352df.IdNAME, 'utf8')), JSON.parse(_0x4d7ed4.readFileSync('' + _0xd352df.IdNAME8 || '' + _0xd352df.IdNAME, 'utf8'))];
        let _0x27c57f = [];
        _0x328557.forEach((_0x257464, _0x20f2d3) => {
          !function _0x428cde(_0xf65361, _0x56a437) {
            _0x442e23({
              'appState': _0xf65361,
              'userAgent': _0x423fa1[_0x56a437],
              'forceLogin': true,
              'httpOptions': {
                'agent': _0x242c6a
              }
            }, (_0x307e1b, _0x2e1fed) => {
              if (_0x307e1b) {
                console.log("Error logging in with account " + (_0x56a437 + 1) + ", retrying...");
                _0x428cde(_0xf65361, _0x56a437);
              } else {
                _0x27c57f[_0x56a437] = _0x2e1fed;
              }
            });
          }(_0x257464, _0x20f2d3);
        });
        let _0x57cd95 = 0;
        _0x177d0f.get(["Select20targetIDs"], function (_0x1155aa, _0x4ee09c) {
          if (_0x1155aa) {
            return _0x4f8ee7(_0x1155aa);
          }
          switch (_0x4ee09c.Select20targetIDs) {
            case '1':
              _0x177d0f.get(["targetID", "short", "file", "timer"], function (_0x29cc4a, _0x5bdf3f) {
                if (_0x29cc4a) {
                  return _0x4f8ee7(_0x29cc4a);
                }
                let _0x219bf2 = _0x4d7ed4.readFileSync(_0x5bdf3f.file, 'utf8').split("\n").filter(Boolean);
                let _0x1a7329 = 0;
                setInterval(() => {
                  let _0x366624 = _0x5bdf3f.short + _0x219bf2[_0x1a7329];
                  _0x27c57f[_0x57cd95].sendMessage(_0x366624, _0x5bdf3f.targetID, () => {});
                  if (++_0x1a7329 >= _0x219bf2.length) {
                    _0x1a7329 = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x5bdf3f.timer + "000");
              });
              break;
            case '2':
              _0x177d0f.get(["targetID", "short", "file1", "targetID2", "short2", 'file2', "timer"], function (_0x37ee9a, _0x21a0f5) {
                if (_0x37ee9a) {
                  return _0x4f8ee7(_0x37ee9a);
                }
                let _0x2e8f0a = _0x4d7ed4.readFileSync(_0x21a0f5.file1, 'utf8').split("\n").filter(Boolean);
                let _0x20dd57 = _0x4d7ed4.readFileSync(_0x21a0f5.file2, 'utf8').split("\n").filter(Boolean);
                let _0x476833 = 0;
                let _0x58896e = 0;
                setInterval(() => {
                  let _0x6da24b = _0x21a0f5.short + _0x2e8f0a[_0x476833];
                  let _0x268b9e = _0x21a0f5.short2 + _0x20dd57[_0x58896e];
                  _0x27c57f[_0x57cd95].sendMessage(_0x6da24b, _0x21a0f5.targetID, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x268b9e, _0x21a0f5.targetID2, () => {});
                  _0x476833++;
                  _0x58896e++;
                  if (_0x476833 >= _0x2e8f0a.length) {
                    _0x476833 = 0;
                  }
                  if (_0x58896e >= _0x20dd57.length) {
                    _0x58896e = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x21a0f5.timer + "000");
              });
              break;
            case '3':
              _0x177d0f.get(["targetID", "short", "file1", "targetID2", "short2", 'file2', 'targetID3', 'short3', "file3", "timer"], function (_0x218b48, _0x347373) {
                if (_0x218b48) {
                  return _0x4f8ee7(_0x218b48);
                }
                let _0x37417f = _0x4d7ed4.readFileSync(_0x347373.file1, 'utf8').split("\n").filter(Boolean);
                let _0x29ca55 = _0x4d7ed4.readFileSync(_0x347373.file2, 'utf8').split("\n").filter(Boolean);
                let _0x361a47 = _0x4d7ed4.readFileSync(_0x347373.file3, 'utf8').split("\n").filter(Boolean);
                let _0x1c3e71 = 0;
                let _0x5b1657 = 0;
                let _0x4a666e = 0;
                setInterval(() => {
                  let _0x3e08eb = _0x347373.short + _0x37417f[_0x1c3e71];
                  let _0xd2a3de = _0x347373.short2 + _0x29ca55[_0x5b1657];
                  let _0xc2708e = _0x347373.short3 + _0x361a47[_0x4a666e];
                  _0x27c57f[_0x57cd95].sendMessage(_0x3e08eb, _0x347373.targetID, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0xd2a3de, _0x347373.targetID2, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0xc2708e, _0x347373.targetID3, () => {});
                  _0x1c3e71++;
                  _0x5b1657++;
                  _0x4a666e++;
                  if (_0x1c3e71 >= _0x37417f.length) {
                    _0x1c3e71 = 0;
                  }
                  if (_0x5b1657 >= _0x29ca55.length) {
                    _0x5b1657 = 0;
                  }
                  if (_0x4a666e >= _0x361a47.length) {
                    _0x4a666e = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x347373.timer + "000");
              });
              break;
            case '4':
              _0x177d0f.get(["targetID", "short", "file1", "targetID2", "short2", "file2", 'targetID3', 'short3', "file3", "targetID4", "short4", 'file4', "timer"], function (_0x19f44c, _0x9806e8) {
                if (_0x19f44c) {
                  return _0x4f8ee7(_0x19f44c);
                }
                let _0x1da25c = _0x4d7ed4.readFileSync(_0x9806e8.file1, 'utf8').split("\n").filter(Boolean);
                let _0x1a0d5b = _0x4d7ed4.readFileSync(_0x9806e8.file2, "utf8").split("\n").filter(Boolean);
                let _0x28d5e1 = _0x4d7ed4.readFileSync(_0x9806e8.file3, 'utf8').split("\n").filter(Boolean);
                let _0x45adcb = _0x4d7ed4.readFileSync(_0x9806e8.file4, 'utf8').split("\n").filter(Boolean);
                let _0x9f37ae = 0;
                let _0x58acba = 0;
                let _0x462bb7 = 0;
                let _0x2dfb28 = 0;
                setInterval(() => {
                  let _0xb245b9 = _0x9806e8.short + _0x1da25c[_0x9f37ae];
                  let _0x4e88fd = _0x9806e8.short2 + _0x1a0d5b[_0x58acba];
                  let _0x477867 = _0x9806e8.short3 + _0x28d5e1[_0x462bb7];
                  let _0x1e8729 = _0x9806e8.short4 + _0x45adcb[_0x2dfb28];
                  _0x27c57f[_0x57cd95].sendMessage(_0xb245b9, _0x9806e8.targetID, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x4e88fd, _0x9806e8.targetID2, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x477867, _0x9806e8.targetID3, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x1e8729, _0x9806e8.targetID4, () => {});
                  _0x9f37ae++;
                  _0x58acba++;
                  _0x462bb7++;
                  _0x2dfb28++;
                  if (_0x9f37ae >= _0x1da25c.length) {
                    _0x9f37ae = 0;
                  }
                  if (_0x58acba >= _0x1a0d5b.length) {
                    _0x58acba = 0;
                  }
                  if (_0x462bb7 >= _0x28d5e1.length) {
                    _0x462bb7 = 0;
                  }
                  if (_0x2dfb28 >= _0x45adcb.length) {
                    _0x2dfb28 = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x9806e8.timer + "000");
              });
              break;
            case '5':
              _0x177d0f.get(["targetID", 'short', "file1", "targetID2", "short2", "file2", 'targetID3', 'short3', "file3", "targetID4", "short4", 'file4', "targetID5", "short5", "file5", "timer"], function (_0x566dd0, _0x5b72e8) {
                if (_0x566dd0) {
                  return _0x4f8ee7(_0x566dd0);
                }
                let _0x2aed44 = _0x4d7ed4.readFileSync(_0x5b72e8.file1, "utf8").split("\n").filter(Boolean);
                let _0x3cf9f4 = _0x4d7ed4.readFileSync(_0x5b72e8.file2, 'utf8').split("\n").filter(Boolean);
                let _0x3ed0d8 = _0x4d7ed4.readFileSync(_0x5b72e8.file3, 'utf8').split("\n").filter(Boolean);
                let _0xfc5eb5 = _0x4d7ed4.readFileSync(_0x5b72e8.file4, 'utf8').split("\n").filter(Boolean);
                let _0x4fdc21 = _0x4d7ed4.readFileSync(_0x5b72e8.file5, 'utf8').split("\n").filter(Boolean);
                let _0xdcbaff = 0;
                let _0x49e7ee = 0;
                let _0x4ce610 = 0;
                let _0x2875c1 = 0;
                let _0x5a65bc = 0;
                setInterval(() => {
                  let _0x1fdd28 = _0x5b72e8.short + _0x2aed44[_0xdcbaff];
                  let _0xaeecfd = _0x5b72e8.short2 + _0x3cf9f4[_0x49e7ee];
                  let _0x3b746f = _0x5b72e8.short3 + _0x3ed0d8[_0x4ce610];
                  let _0x38a192 = _0x5b72e8.short4 + _0xfc5eb5[_0x2875c1];
                  let _0x15fb49 = _0x5b72e8.short5 + _0x4fdc21[_0x5a65bc];
                  _0x27c57f[_0x57cd95].sendMessage(_0x1fdd28, _0x5b72e8.targetID, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0xaeecfd, _0x5b72e8.targetID2, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x3b746f, _0x5b72e8.targetID3, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x38a192, _0x5b72e8.targetID4, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x15fb49, _0x5b72e8.targetID5, () => {});
                  _0xdcbaff++;
                  _0x49e7ee++;
                  _0x4ce610++;
                  _0x2875c1++;
                  _0x5a65bc++;
                  if (_0xdcbaff >= _0x2aed44.length) {
                    _0xdcbaff = 0;
                  }
                  if (_0x49e7ee >= _0x3cf9f4.length) {
                    _0x49e7ee = 0;
                  }
                  if (_0x4ce610 >= _0x3ed0d8.length) {
                    _0x4ce610 = 0;
                  }
                  if (_0x2875c1 >= _0xfc5eb5.length) {
                    _0x2875c1 = 0;
                  }
                  if (_0x5a65bc >= _0x4fdc21.length) {
                    _0x5a65bc = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x5b72e8.timer + "000");
              });
              break;
            case '6':
              _0x177d0f.get(["targetID", "short", "file1", "targetID2", "short2", 'file2', 'targetID3', 'short3', "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", 'file6', "timer"], function (_0x22e133, _0x43e5e8) {
                if (_0x22e133) {
                  return _0x4f8ee7(_0x22e133);
                }
                let _0x53afbe = _0x4d7ed4.readFileSync(_0x43e5e8.file1, 'utf8').split("\n").filter(Boolean);
                let _0x25ad34 = _0x4d7ed4.readFileSync(_0x43e5e8.file2, 'utf8').split("\n").filter(Boolean);
                let _0x2e5e23 = _0x4d7ed4.readFileSync(_0x43e5e8.file3, "utf8").split("\n").filter(Boolean);
                let _0x502de4 = _0x4d7ed4.readFileSync(_0x43e5e8.file4, 'utf8').split("\n").filter(Boolean);
                let _0x187958 = _0x4d7ed4.readFileSync(_0x43e5e8.file5, 'utf8').split("\n").filter(Boolean);
                let _0x46801b = _0x4d7ed4.readFileSync(_0x43e5e8.file6, "utf8").split("\n").filter(Boolean);
                let _0x252547 = 0;
                let _0x17aea1 = 0;
                let _0x16e677 = 0;
                let _0x4f11e2 = 0;
                let _0x979cbe = 0;
                let _0x546b47 = 0;
                setInterval(() => {
                  let _0x169fa6 = _0x43e5e8.short + _0x53afbe[_0x252547];
                  let _0x3ce6c5 = _0x43e5e8.short2 + _0x25ad34[_0x17aea1];
                  let _0x2d1665 = _0x43e5e8.short3 + _0x2e5e23[_0x16e677];
                  let _0x318848 = _0x43e5e8.short4 + _0x502de4[_0x4f11e2];
                  let _0x267347 = _0x43e5e8.short5 + _0x187958[_0x979cbe];
                  let _0x18bd59 = _0x43e5e8.short6 + _0x46801b[_0x546b47];
                  _0x27c57f[_0x57cd95].sendMessage(_0x169fa6, _0x43e5e8.targetID, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x3ce6c5, _0x43e5e8.targetID2, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x2d1665, _0x43e5e8.targetID3, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x318848, _0x43e5e8.targetID4, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x267347, _0x43e5e8.targetID5, () => {});
                  _0x27c57f[_0x57cd95].sendMessage(_0x18bd59, _0x43e5e8.targetID6, () => {});
                  _0x252547++;
                  _0x17aea1++;
                  _0x16e677++;
                  _0x4f11e2++;
                  _0x979cbe++;
                  _0x546b47++;
                  if (_0x252547 >= _0x53afbe.length) {
                    _0x252547 = 0;
                  }
                  if (_0x17aea1 >= _0x25ad34.length) {
                    _0x17aea1 = 0;
                  }
                  if (_0x16e677 >= _0x2e5e23.length) {
                    _0x16e677 = 0;
                  }
                  if (_0x4f11e2 >= _0x502de4.length) {
                    _0x4f11e2 = 0;
                  }
                  if (_0x979cbe >= _0x187958.length) {
                    _0x979cbe = 0;
                  }
                  if (_0x546b47 >= _0x46801b.length) {
                    _0x546b47 = 0;
                  }
                  if (++_0x57cd95 === _0x27c57f.length) {
                    _0x57cd95 = 0;
                  }
                }, _0x43e5e8.timer + "000");
              });
              break;
            case '7':
              _0x177d0f.get(["targetID", "short", "file1", "targetID2", "short2", "file2", 'targetID3', 'short3', "file3", "targetID4", "short4", "file4", "targetID5", "short5", "file5", "targetID6", "short6", 'file6', 'targetID7', 'short7', "file7", "timer"], function (_0x40c227, _0x34dc0e) {
                if (_0x40c227) {
                  return _0x4f8ee7(_0x40c227);
                }
                let _0x29968b = _0x4d7ed4.readFileSync(_0x34dc0e.file1, 'utf8').split("\n").filter(Boolean);
                let _0x3fda43 = _0x4d7ed4.readFileSync(_0x34dc0e.file2, 'utf8').split("\n").filter(Boolean);
                let _0x5e9887 = _0x4d7ed4.readFileSync(_0x34dc0e.file3, 'utf8').split("\n").filter(Boolean);
                let _0x1b3a7d = _0x4d7ed4.readFileSync(_0x34dc0e.file4, 'utf8').split("\n").filter(Boolean);
                let _0x49637a = _0x4d7ed4.readFileSync(_0x34dc0e.file5, 'utf8').split("\n").filter(Boolean);
                let _0x3bf4d5 = _0x4d7ed4.readFileSync(_0x34dc0e.file6, 'utf8').split("\n").filter(Boolean);
                let _0xf56aca = _0x4d7ed4.readFileSync(_0x34dc0e.file7, 'utf8').split("\n").filter(Boolean);
                let _0x421231 = 0;
                let _0x5a3731 = 0;
                let _0x9c34b5 = 0;
                let _0x4735e2 = 0;
                let _0x41e5ea = 0;
                let _0x21caf5 = 0;
                let _0x127cb1 = 0;
                setInterval(() => {
                  let _0x4aa79c = _0x34dc0e.short + _0x29968b[_0x421231];
                  let _0x3de21f = _0x34dc0e.short2 + _0x3fda43[_0x5a3731];
                  let _0x3cc667 = _0x34dc0e.short3 + _0x5e9887[_0x9c34b5];
       
