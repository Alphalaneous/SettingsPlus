strInput = """if (gv == "0026") ret = "Restarts level upon death automatically.";
if (gv == "0052") ret = "Restarts in 0.5 s instead of 1.0 s upon death.";
if (gv == "0128") ret = "Locks and hides cursor during gameplay.";
if (gv == "0010") ret = "Flips which side controls which player during 2-player mode.";
if (gv == "0011") ret = "Limits player 1 controls to one side even when dual mode is inactive.";
if (gv == "0028") ret = "Disables mouse movement when using a controller thumbstick.";
if (gv == "0163") ret = "Enables some quick temporary bindings until full customization later. Use 'R' for reset, 'CTRL + R' for full reset, and 'P' to toggle hitboxes in Practice mode.";
if (gv == "0024") ret = "Shows cursor and pause button during gameplay.";
if (gv == "0135") ret = "Hides the attempt counter when playing levels.";
if (gv == "0015") ret = "Flips the location of the pause button.";
if (gv == "0129") ret = "Disables extra indicators on portals.";
if (gv == "0130") ret = "Enables extra indicators on orbs.";
if (gv == "0140") ret = "Disables the scaling effect on all orbs.";
if (gv == "0141") ret = "Disables the scaling effect on only trigger orbs.";
if (gv == "0172") ret = "Disables shake effects.";
if (gv == "0014") ret = "Disables the shake effect that happens upon death.";
if (gv == "0072") ret = "Disables the effect that happens upon changing gravity.";
if (gv == "0060") ret = "Sets player icon in mini mode to default.";
if (gv == "0061") ret = "Toggles between main and secondary color for the teleport effect in spider mode.";
if (gv == "0062") ret = "Toggles between main and secondary color for the fire effect from dash orbs.";
if (gv == "0096") ret = "Toggles between main and secondary color for the trail in wave mode.";
if (gv == "0174") ret = "Hides text in the top left when using start positions or ignore damage.";
if (gv == "0071") ret = "Hides the checkpoint buttons shown in practice mode.";
if (gv == "0134") ret = "Hides the attempt counter when playing levels in practice mode.";
if (gv == "0027") ret = "Places checkpoints automatically in practice mode.";
if (gv == "0068") ret = "Tries to place checkpoints more often in practice mode.";
if (gv == "0100") ret = "Shows death effects in practice mode.";
if (gv == "0125") ret = "Plays normal music in sync to editor levels in practice mode.";
if (gv == "0166") ret = "Shows hitboxes while in practice mode.";
if (gv == "0171") ret = "Disables the player's hitbox in practice mode (if hitboxes are shown).";
if (gv == "0066") ret = "Increases draw capacity for batch nodes at level start. Can improve performance on some levels, but may cause issues on low-end devices.";
if (gv == "0108") ret = "Enables low detail mode on levels that support it automatically.";
if (gv == "0082") ret = "Removes the alert shown when starting levels with a high object count.";
if (gv == "0136") ret = "Removes glow and enter effects while in low detail mode. Levels without LDM show LDM Lite.";
if (gv == "0042") ret = "Increases maximum locally saved levels from 10 to 100. This refers to level data, not statistics. Enabling this can make your save file considerably larger, so keeping the option off is recommended for quicker saving.";
if (gv == "0119") ret = "Saves level statistics as usual, but levels need to be redownloaded every time you restart the game. Makes saving and loading faster.";
if (gv == "0127") ret = "Saves gauntlet levels locally so they do not have to be redownloaded. Increases save time but helpful if you have poor connection.";
if (gv == "0155") ret = "Disables anti-aliasing on shader effects.";
if (gv == "0033") ret = "Saves custom songs in a different directory. May fix custom songs not working.";
if (gv == "0083") ret = "Removes the alert shown when starting levels without the song downloaded.";
if (gv == "0018") ret = "Stops automatic deletion of custom songs. This is done by default to save space.";
if (gv == "0142") ret = "Lowers audio sampling rate from 44100 Hz to 24000 Hz. Requires restarting to take effect.";
if (gv == "0159") ret = "Increases the audio buffer size, which may fix certain issues. Do not enable if audio is working fine. Causes a slight more audio delay. Requires restarting to take effect.";
if (gv == "0094") ret = "Shows more comments per page. Why not?";
if (gv == "0090") ret = "Loads comments automatically.";
if (gv == "0073") ret = "Makes completed levels filter based only on percentage from update 2.1. Useful to rebeat levels for Mana Orbs.";
if (gv == "0093") ret = "Increases created and saved levels per page from 10 to 20.";
if (gv == "0084") ret = "Places new levels last in the saved levels list. Useful if you want to manually move levels to the top.";
if (gv == "0126") ret = "Shows decimals in level progress.";
if (gv == "0099") ret = "Toggles viewing the leaderboard percentage you have on levels. To upload your level progress to the level leaderboard, you need to replay levels completed before 2.11.";
if (gv == "0095") ret = "Does not do anything... Well, nothing useful.";
if (gv == "0167") ret = "Adds an extra confirmation window when exiting levels.";
if (gv == "0168") ret = "Makes transitions between menu pages faster.";
if (gv == "0040") ret = "Toggles the percent label in game";
if (gv == "0074") ret = "Toggles the restart button on the pause menu";
if (gv == "0109") ret = "Toggles the extra info/debug label in game";
if (gv == "0113") ret = "Flips the platformer controls";
if (gv == "0153") ret = "Whether the player should explode on death";
if (gv == "0022") ret = "Whether the game should use higher audio quality";
if (gv == "0075") ret = "(Parental Controls) Disables comments <cy>(known to be buggy)</c>";
if (gv == "0076") ret = "(Parental Controls) Disables account posts";
if (gv == "0077") ret = "(Parental Controls) Removes the featured levels button in the creator menu";
if (gv == "0023") ret = "Toggles smooth fix";
if (gv == "0065") ret = "Toggles move optimization";
if (gv == "0101") ret = "Forces smooth fix to be on";
if (gv == "0102") ret = "Toggles smooth fix in the editor";
if (gv == "0056") ret = "Disables the high object alert";
if (gv == "0081") ret = "Disables the shake effect in levels";
if (gv == "0067") ret = "Increases the accuracy of start positions";""".replace("if (gv == \"", "").replace("\") ret = \"", "").replace("\";", "")

for line in strInput.split("\n"):
    gv = line[:4]
    desc = line[-len(line)+4:]
    print("{\"" + gv + "\", \"" + desc + "\"},")