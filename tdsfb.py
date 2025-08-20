
import json, random, traceback # type: ignore
import requests, base64, uuid, os # type: ignore
from time import sleep
# Màu sắc hiển thị
# Get IP from URL
def get_ip_from_url(url):
    try:
        data = requests.get(url).json()
        ip_address = data['ip']
        country = data['country']
        return ip_address, country
    except: 
        ip_address = "Unknown"
        country = "Unknown"
    return ip_address, country
url = "https://api.myip.com/"
ip, country = get_ip_from_url(url)
# Màu
luc =  "\033[1;32m"
trang =  "\033[1;37m"
do =  "\033[1;31m"
vang =  "\033[0;93m"
hong =  "\033[1;35m"
xnhac =  "\033[1;36m" 
xduong = "\033[1;34m"
atuan = f"{do}[{trang}</>{trang}]{do} {hong}➤ {luc}"

# Logo
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo_text = f"""
\033[1;31m █████╗ ███╗   ██╗██╗  ██╗████████╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;37m██╔══██╗████╗  ██║██║  ██║╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
\033[1;31m███████║██╔██╗ ██║███████║   ██║   ██║   ██║███████║██╔██╗ ██║
\033[1;37m██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██║██║╚██╗██║ 
\033[1;31m██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║
\033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;35m      Copyright By: @TaT - eXe 2024 | Version 3.3 
\033[97m----------------------------------------------------------------- 
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;32m Admin: \033[1;33mGiang A Lus x Hac Long De
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;32m Copyright: \033[1;33mTran Anh Tuan (lol)
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;32m Box Tele: \033[1;33mT.me/@share_code_ngon
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;32m Box Zalo: \033[1;33mhttps://zalo.me/g/wbfxsu361
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;32m YouTuBe: \033[1;33mYoutube.com/@sharesrctool
\033[1;31m[\033[1;37m</>\033[1;31m]\033[1;37m =>\033[1;35m Chào Mừng Bạn Đã Đến Với Tool
\033[97m----------------------------------------------------------------- """
    print(logo_text)
logo()
def countdown_(delay):
    for remaining in range(delay, 0, -1):
        for _ in range(5):  # Tăng tốc hiệu ứng "x" bằng cách hiển thị 5 lần mỗi giây
            effect = "".join(random.choice(["𝐗", " "]) for _ in range(5))  # Chuỗi "x" ngẫu nhiên
            print(f" \r{do}[{vang}T{do}] {do}[{trang}Countdown{do}] {do}[{luc}{effect}{do}] [{xnhac}{remaining}{do}]                         \r", end='')
            sleep(0.2)  # Giảm thời gian chờ để hiệu ứng nhanh hơn
    print("\r\r\033[1;95m    ⚡T-TOOL⚡\033[1;37m                         \r", end='')
    print(" "*65, end="\r")
def loadjob(delay):
    for remaining in range(delay, 0, -1):
        for _ in range(5):  # Tăng tốc hiệu ứng "x" bằng cách hiển thị 5 lần mỗi giây
            effect = "".join(random.choice(["𝐗", " "]) for _ in range(5))  # Chuỗi "x" ngẫu nhiên
            print(f" \r{do}[{vang}HB{do}] {do}[{trang}Load_Job{do}] {do}[{luc}{effect}{do}] [{xnhac}{remaining}{do}]                         \r", end='')
            sleep(0.2)  # Giảm thời gian chờ để hiệu ứng nhanh hơn
    print("\r\r\033[1;95m    ⚡T-TOOL⚡\033[1;37m                         \r", end='')
    print(" "*65, end="\r")
def DelayTime(delay):
    for remaining in range(delay, 0, -1):
        for _ in range(5):  # Tăng tốc hiệu ứng "x" bằng cách hiển thị 5 lần mỗi giây
            effect = "".join(random.choice(["𝐗", " "]) for _ in range(5))  # Chuỗi "x" ngẫu nhiên
            print(f" \r{do}[{vang}HB{do}] {do}[{trang}Delay{do}] {do}[{luc}{effect}{do}] [{xnhac}{remaining}{do}]                         \r", end='')
            sleep(0.2)  # Giảm thời gian chờ để hiệu ứng nhanh hơn
    print("\r\r\033[1;95m    ⚡T-TOOL⚡\033[1;37m                         \r", end='')
    print(" "*65, end="\r")
def gio_vn():
    from datetime import datetime

    # Lấy giờ hiện tại
    now = datetime.now()

    # Định dạng và hiển thị giờ
    current_time = now.strftime("%H:%M:%S")
    return current_time
def thanh_ngang():
    print('\033[1;31m─\033[1;37m'*57+"                      ")
# API FACEBOOK
class Facebook_API:
    def __init__(self, cookie):
        self.cookie = cookie
        self.session = requests.Session()
        self.headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
            'Cookie': self.cookie
        }
        self.idfb, self.name, self.jazoest, self.fb_dtsg = self.get_profile_data()

    def get_profile_data(self):
        url = 'https://www.facebook.com/profile.php'
        try:
            res = self.session.get(url, cookies={'cookie': self.cookie}).text
            name_ = res.split('","NAME":"')[1].split('"')[0]
            name__ = name_.encode('utf-8', 'ignore').decode('utf-8')
            name = json.loads(str(f'"{name__}"'))
            idfb = self.cookie.split('c_user=')[1].split(';')[0]
            jazoest = res.split('jazoest=')[1].split('"')[0]
            fb_dtsg = res.split('"f":"')[1].split('"')[0]
            link_die = self.session.get(url, headers=self.headers).url
            if "601051028565049" in link_die:
                data = {
                    'av': idfb,
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'FBScrapingWarningMutation',
                    'variables': '{}',
                    'server_timestamps': 'true',
                    'doc_id': '6339492849481770',
                }
                self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
                sleep(2)
            return idfb, name, jazoest, fb_dtsg
        except:
            return None, None, None, None

    def reaction(self, post_id, reaction_type):
        try:
            feedback_id = base64.b64encode(f"feedback:{post_id}".encode()).decode()
            reac = {
                "LIKE": "1635855486666999",
                "LOVE": "1678524932434102",
                "CARE": "613557422527858",
                "HAHA": "115940658764963",
                "WOW": "478547315650144",
                "SAD": "908563459236466",
                "ANGRY": "444813342392137"
            }
            idreac = reac.get(reaction_type.upper())
            if not idreac:
                print(f"[!] Không tìm thấy loại cảm xúc '{reaction_type}'!")
                return False

            data = {
                'av': self.idfb,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{feedback_id}","feedback_reaction_id":"{idreac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":[],"session_id":"{uuid.uuid4()}","actor_id":"{self.idfb}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
                'server_timestamps': 'true',
                'doc_id': '7047198228715224',
            }

            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
            if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
                return True
            else:
                return False
        except:
            return False
    def follow(self, subscribee_id):
        data = {
            'av': self.idfb,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1734253880726,902779,250100865708545,,;CometHomeRoot.react,comet.home,logo,1734253816004,586394,4748854339,3#3#230#301,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+str(subscribee_id)+'","tracking":null,"actor_id":"'+self.idfb+'","client_mutation_id":"7"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '28167180839546919',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if """{"data":{"actor_subscribe":{"subscribee":{"__typename":"User","profile_action":{"__typename":"ProfileActionFollow","__isProfileAction":"ProfileActionFollow",""" in response:
            return True
        else:
            return False
    def cmt(self, post_id, msg):
        uuid1 = uuid.uuid4()
        uuid2 = uuid.uuid4()
        feedback_id = base64.b64encode(f"feedback:{post_id}".encode()).decode()
        data = {
            'av': self.idfb,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
            'variables': '{"feedLocation":"NEWSFEED","feedbackSource":1,"groupID":null,"input":{"client_mutation_id":"2","actor_id":"'+self.idfb+'","attachments":null,"feedback_id":"'+feedback_id+'","formatting_style":null,"message":{"ranges":[],"text":"'+msg+'"},"attribution_id_v2":"CometHomeRoot.react,comet.home,logo,1741357306608,148760,4748854339,,","vod_video_timestamp":null,"is_tracking_encrypted":true,"tracking":["AZUX8JJiSQmTaZs-h65hzFeff8m9ThcqQFfU8CSYxHVFJRHKriVG1iDgfQfqcQjh7RKCa4GkCxNyLJwnmKOC-Kb1_bgB6uG5F_OdB6Rs4a5qVd-duGZqjMss066BOJip6nXt1beDKHDUQZStc-tiK78PdZEvzOfv45B1K7VXLzt_41-qRbHFwFpjvDAQAWdhF5ynbRuUgsMbUhXR51XhmS_KpxzI_ri4sQwiWO2EjrwaIDMMjvE0iSv3sNac-7JtHfKDE77NiIm3_snIHHL_BEwYFGjF0O-DssAeJdvEoNiWFhntss9o87rPC138sW01GWR72BNCUwQw1YvIgf-d_GD8NEVuZ4kgvMeW_9m3069Oe_LnOM86P57WW6oIMVjlwydFftGw2iJb5KklFumWCU8mVCJ7hM7meDBi4rkYc9ceX3bgLK-LELTzNGj13wyVUexGOwxcJ85AkV9wsYS_LKRWLzX6bpkKvgBVhcByxWBzSler7ggsOf6wcHpyfz4Vw_uGm4_qbxrNlPu8YeeeGO-iRvl3wVrKQrJ4XNyaksPYSsBNGjMl6LG3PIU7iexJJymKWMlB7QSi6AJsr4vfhxLQavEmu_NI_7RDixHfWSWpENERp42sm0VsRY-Zf68Go5g4827Jh3OEPvIMgmofx1H69qi5yIFtchlCftBePVL_o6inIyxll00sZrK4jEEWr6DiBPYxSdLGNNzplyumYaOpy3g26nwDC0i0ROs8TbU1NTwVfoLGUv2rymo3-4Kf4EkeDngCT_-KoCMubpfXKPC2FVmDmC2vGSonrMnBz5RiozBgAqBEDmuH-h8keBPEgoR1oe7dH0RjFdaD33cNHIaEycVkZOr6Ky4PZGqvtPZEyrNKlKvapsAo7psuNdeEGvq_o29MvsMuRWn2NqWzLzhn_GOBly_RrFeuXwfIb6N-l6Xe5LrGyY_0qEZkpMksxsImsPhAfUmz2xYL3Kxb_tK2X90IvEODf4Gv6hrdjMb2MAMEwbi74tZf8ZVHqb-VLLyWAFm-sSC2sX44Ri8W2fuJcvau_pptR3E7HStfThssfUwAT_SpGfxNKLs99rh-KiYSfDe5mrTeKyQ2s-_-xQf1aBMkGkiOXaSC24tL2xYxej9pDQKWRuXILkiwhlmBLDw0YmEXe4H-vB2mlxN8ndYvEZCXLH1RAkVV7GmbyG_ovDllJxK3PsTMwoMIh4rHXbTBsBq0_hh0mGF6E4Z_ZC_zNHniP1FlpTYAa9-kBMiNoIibYgv4VH7axrrZtWyX7OHlD11cO2y8C2AOByTiOgxoyDkoKHtShBpH9AolHMNx2aSvHrU6ALCaz6k8AFarwhIn0tp2z79EQ4a3W2iP-HjtfxC7lut3GWw-Exg9fBAB7_CgYOs-ZMCTuU1WmWdeGCL-O4wm0p4HcnuL8wUO4h_I0-cFsera5OAmk3OIFVtIko5rgZnlxBWC6RkB-eZr7Dgpt5xvXPa_sbtk9rE9v8dIB0i8xn9F0Asb9iROiCKAptLGkMqwYNaazAuNN5kSL_P5y2sCZYcJpLUmmtSCQkij1VXeL2h3t77e1-_i3MienR-wirNO8XHoqfTKs8-2T8u-XFT27NKv-c37NGavH6WDUOQCS6AxXqOljhplwSDM2YJFhwijHPkDP4c4sk44mQkh--smFhI2U8bGsj7oGBq7B6rhPb1TVf5TtrbRxuuolD9hIPlp0c401E6NwfnGFQpy9V1vbLe8DqcNIevmL92gZ-FsVJ2iLesy9wgm_i-dlObKKN_JjVf9f9T3kw1nXCHirVUMdMMFlkRJEGtiKl7KcjxOV7B8SteGbPeTA0rvdUYKMeavaA59Bf9fUb_9lWGJDL3UssKa-4pp8YGv2yKRi4HQYLVV2OweN2w8MgumtnnT4bLg6TMKWF4xI1-ScH2Y2CP1uatIICuBFGq0jY6PBac6D3zaSAagjcZlT7PpuVkgnDPnvjXCwVVP97QZ07LCMF7aw71S069qssuSD9nd6H7hngFgDnzDHnPFethUbExWoBWTEvRkqD4qfwrrDh03YJXaqEDzF9ATU4_wZOGW9swVmQb5L2XsA9DRtPMhQQ","{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":null,\\"conversation_guide_shown\\":null}"],"feedback_source":"NEWS_FEED","idempotence_token":"client:'+str(uuid1)+'","session_id":"'+str(uuid2)+'"},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null,"__relay_internal__pv__IsWorkUserrelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '9345503868819301',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if '{"data":{"comment_create":{"feedback":' in response:
            return True
        else:
            return False
    def share(self, post_id, msg):
        data = {
            'av': self.idfb,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
            'variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"'+str(uuid.uuid4())+'_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+post_id+']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":[null],"message":{"ranges":[],"text":"'+msg+'"},"logging":{"composer_session_id":"'+str(uuid.uuid4())+'"},"navigation_data":{"attribution_id_v2":"CometTahoeRoot.react,comet.videos.tahoe,via_cold_start,1740883384212,705957,2392950137,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"'+self.idfb+'","client_mutation_id":"1"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '9212136468841650',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if '{"data":{"story_create":{"story_id":' in response:
            return True
        else:
            return False
    def page(self, id_page):
        data = {
            'av': self.idfb,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
            'variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+id_page+'","source":null,"tracking":null,"actor_id":"'+self.idfb+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6716077648448761',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if '{"data":{"page_like":{"page":' in response:
            return True
        else:
            return False
    def group(self, id_group):
        data = {
            'av': self.idfb,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+id_group+'","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1744345022184,11025,2361831622,,","group_id":"'+id_group+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.idfb+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '9208589639268737',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
        }
        response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if """{"data":{"group_request_to_join":{"viewer":{"groups_tab":{"tab_groups_list":{"edges":[{"node":{"id":""" in response:
            return True
        else:
            return False
    def check_live_uid(self, post_id):
        url = self.session.get(f'https://www.facebook.com/{post_id}', headers=self.headers).url
        if url == f"https://www.facebook.com/{post_id}": return "UID_DIE"
        if '1501092823525282' in url: return "282"
        if '828281030927956' in url: return "956"
        if "601051028565049" in url:
            data = {
                'av': self.idfb,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FBScrapingWarningMutation',
                'variables': '{}',
                'server_timestamps': 'true',
                'doc_id': '6339492849481770',
            }
            self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
            sleep(2)
            url = self.session.get(f'https://www.facebook.com/{post_id}', headers=self.headers).url
            if url == f"https://www.facebook.com/{post_id}": return "UID_DIE"
        return "UID_LIVE"

# API Trao Đổi Sub
class TDS_API:
    def __init__(self, token): self.token = token; self.base_url = "https://traodoisub.com/api/"
    def request(self, path): url = f"{self.base_url}{path}&access_token={self.token}"; response = requests.get(url); return response.json()
    def profile(self): return self.request("?fields=profile")
    def cau_hinh(self, idfb): return self.request(f"?fields=run&id={idfb}")
    def get_jobs(self, job): return self.request(f"?fields={job}")
    def nhan_xu(self, job, job_id): return self.request(f"coin/?type={job}&id={job_id}")

TASKS = {
    "1": ("facebook_reaction", "Reaction Vip"),
    "2": ("facebook_reaction2", "Reaction2"),
    "3": ("facebook_reactioncmt", "Reactioncmt"),
    "4": ("facebook_share", "Share"),
    "5": ("facebook_follow", "Follow"),
    "6": ("facebook_page", "Like Page"),
}

def show_task_menu():
    print(f"{atuan}Chọn Loại Nhiệm Vụ {do}({luc}Ví Dụ: {vang}1,2,5{do})")
    [print(f"{atuan}Nhập {do}[{vang}{k}{do}] {luc}{v[1]}") for k, v in TASKS.items()]
    print(f"{atuan}Nhập {do}[{vang}X{do}] {luc}All Nhiệm Vụ")
    chon = input(f"{atuan}Nhập Số: {vang}").split(",")
    return [v[0] for k, v in TASKS.items() if k in chon or "x" in chon or "X" in chon]

def read_file(f): return open(f, "r", encoding="utf-8").read().strip() if os.path.exists(f) else ""
def save_file(f, c): open(f, "w", encoding="utf-8").write(c.strip())
def mask_id(insta_id: str) -> str: return insta_id[:3] + '#' * (len(insta_id) - 6) + insta_id[-3:]
def main():
    token_file = "Access_Token_TDS.txt"
    old_token = read_file(token_file)
    user = xu = xudie = None

    if old_token:
        tds = TDS_API(old_token)
        profile = tds.profile()
        if 'error' in profile: old_token = None
        elif profile.get('success') == 200: user = profile['data']['user']; xu = profile['data']['xu']; xudie = profile['data']['xudie']
        else: old_token = None

    if not old_token:
        token = input(f"{atuan} Nhập Access Token TDS: {vang}")
        tds = TDS_API(token)
        profile = tds.profile()
        if 'error' in profile: print(atuan+do, profile['error']); return
        elif profile.get('success') == 200: user = profile['data']['user']; xu = profile['data']['xu']; xudie = profile['data']['xudie']; save_file(token_file, token)
        else: return

    else:
        print(f"{atuan}Nhập {do}[{vang}1{do}] {luc}Giữ Tài Khoản {vang}{user}")
        print(f"{atuan}Nhập {do}[{vang}2{do}] {luc}Nhập Access Token TDS Mới")
        if input(f"{atuan}Nhập Lựa Chọn: {vang}") == "2":
            token = input(f"{atuan}Nhập Access Token TDS: {vang}")
            tds = TDS_API(token)
            profile = tds.profile()
            if 'error' in profile: print(atuan+do, profile['error']); return
            elif profile.get('success') == 200: user = profile['data']['user']; xu = profile['data']['xu']; xudie = profile['data']['xudie']; save_file(token_file, token)
            else: return

    # In thông tin tài khoản
    thanh_ngang()
    print(f"{atuan}Tài Khoản: {vang}{user}")
    print(f"{atuan}Xu Hiện tại: {vang}{xu}")
    print(f"{atuan}Xu Die: {vang}{xudie}")
    thanh_ngang()

    # === Nhập danh sách cookie Facebook ===
    list_clone, stt = [], 0
    while True:
        stt += 1
        cookie_fb = input(f'{atuan}Nhập Cookie Facebook Thứ {xnhac}{stt}: {vang}')
        if cookie_fb == '': break
        fb = Facebook_API(cookie_fb)
        if not all([fb.idfb, fb.fb_dtsg, fb.jazoest]): print(f"{atuan}{do}COOKIE DIE HOẶC LỖI LẤY THÔNG TIN. VUI LÒNG NHẬP LẠI."); stt -= 1
        else: print(f"{luc}Id Facebook: {vang}{fb.idfb} {do}</> {luc}Tên Tài Khoản: {vang}{fb.name}"); list_clone.append(cookie_fb); thanh_ngang()

    # === Cấu hình nhiệm vụ ===
    logo()
    print(f"{atuan}Tài Khoản: {vang}{user}")
    print(f"{atuan}Xu Hiện Tại: {vang}{xu}")
    print(f"{atuan}Xu Die: {vang}{xudie}")
    thanh_ngang()

    job_types = show_task_menu()
    if not job_types: print(f"{atuan}{do}MÀY BỊ NGU À :))"); exit()

    thanh_ngang()
    delay = int(input(f"{atuan}Nhập Delay: {vang}"))
    nvblock = int(input(f"{atuan}Sau bao nhiêu nhiệm vụ thì nghỉ: {vang}"))
    delaybl = int(input(f"{atuan}Thời gian nghỉ (giây): {vang}"))
    doiacc = int(input(f"{atuan}Sau bao nhiêu nhiệm vụ thì đổi acc: {vang}"))
    thanh_ngang()
    idx, nvblockx = 0, 0
    error_counts = {}
    seen_jobs = set()
    while True:
        for cookie in list_clone:
            fb = Facebook_API(cookie)
            if not all([fb.idfb, fb.fb_dtsg, fb.jazoest]): print(f"{do} Cookie {vang}{cookie.split('c_user=')[1].split(';')[0]} {do} đã bị die hoặc out"); list_clone.remove(cookie); continue
            else:
                setnick = tds.cau_hinh(fb.idfb)
                if setnick.get('success') == 200: 
                    if setnick['data']['msg'] == "Cấu hình thành công!":
                        print(f"{luc}Id Facebook: {vang}{mask_id(fb.idfb)} {do}</> {luc}Tên Tài Khoản: {vang}{fb.name}")
                else: print(f"{atuan}{do}{setnick}"); continue
                # Khởi tạo lỗi
                if cookie not in error_counts: error_counts[cookie] = {}

                # Kiểm tra bị block toàn bộ nhiệm vụ
                if all(error_counts[cookie].get(job, 0) >= 100 for job in job_types): print(f"{do} Cookie {vang}{fb.name} {do}đã bị block tất cả nhiệm vụ » xóa khỏi list"); list_clone.remove(cookie); continue
                doiaccx = 0
                while True:

                    available_jobs = [job for job in job_types if error_counts[cookie].get(job, 0) < 100]
                    if not available_jobs: print(f"{do} Cookie {vang}{fb.name} đã bị block tất cả nhiệm vụ » xóa khỏi list"); list_clone.remove(cookie); break
                    die_cookie = False
                    #job_type = random.choice(available_jobs)
                    for job_type in available_jobs:
                        if error_counts[cookie].get(job_type, 0) >= 100: print(f"{do} Cookie {vang}{fb.name} bị block nhiệm vụ {job_type}"); continue

                        try: 
                            getjob = tds.get_jobs(job_type)
                        
                            if 'error' in getjob and getjob['error'] == "Thao tác quá nhanh vui lòng chậm lại": countdown_(int(getjob['countdown'])); continue

                            if 'data' not in getjob or not getjob['data']: print(f"{hdang}{do}Không có nhiệm vụ nào.", end='\r'); continue
                            count = len(getjob.get('data', [])) if isinstance(getjob, dict) else 0
                            print(f"{atuan}Tìm thấy{vang} {count}{luc} nhiệm vụ{xduong} {job_type}", end='\r')
                            
                            for job in getjob['data']:
                                
                                if error_counts[cookie].get(job_type, 0) >= 100:
                                    print(f"{do} Cookie {vang}{fb.name} bị block nhiệm vụ {job_type}")
                                    break
                                #print(f"ID: {job.get('id')}, Code: {job.get('code')}, Type: {job.get('type')}")
                                post_id = job.get('id')
                                code = job.get('code')
                                
                                if post_id in seen_jobs:
                                    print(f"{do} {post_id.split('_')[-1] if '_' in post_id else post_id} Đã check job ảo, bỏ qua...       ", end='\r')
                                    continue

                                # Nếu chưa kiểm tra, thì kiểm tra và lưu lại
                                
                                check_uid = fb.check_live_uid(post_id)
                                if check_uid == "UID_DIE":
                                    seen_jobs.add(post_id)
                                    print(f"{do} {post_id.split('_')[-1] if '_' in post_id else post_id} Job ảo, bỏ qua...                ", end='\r')
                                    continue
                                if check_uid == "282":
                                    print(f"{do} Cookie {vang}{cookie.split('c_user=')[1].split(';')[0]} {do} đã bị die 282")
                                    list_clone.remove(cookie)
                                    die_cookie = True
                                    break
                                if check_uid == "956":
                                    print(f"{do} Cookie {vang}{cookie.split('c_user=')[1].split(';')[0]} {do} đã bị die 956")
                                    list_clone.remove(cookie)
                                    die_cookie = True
                                    break
                                if job_type == "facebook_reaction": thuchien = fb.reaction(post_id.split("_")[-1], job.get('type'))
                                elif job_type == "facebook_reaction2": thuchien = fb.reaction(post_id.split("_")[-1], job.get('type'))
                                elif job_type == "facebook_reactioncmt": thuchien = fb.reaction(post_id, job.get('type'))
                                elif job_type == "facebook_share": thuchien = fb.share(post_id, msg="")
                                elif job_type == "facebook_follow": thuchien = fb.follow(post_id)
                                elif job_type == "facebook_page": thuchien = fb.page(post_id)
                                else: print(f"{do}Nhiệm Vụ Không Hợp Lệ", end='\r'); continue
                                
                                idx += 1
                                nvblockx += 1
                                doiaccx += 1
                                status_action = job.get("type", job_type.split('_')[1]).upper()
                                if job_type == "facebook_reaction2": status_action += "2"
                                if job_type == "facebook_reactioncmt": status_action += "CMT"
                                post_display = post_id.split('_')[-1] if '_' in post_id else post_id
                                status = f"{do}[{vang}{idx}{do}][{luc}{gio_vn()}{do}][{xnhac}{status_action}{do}][{hong}{post_display}{do}]"
                                
                                if thuchien:
                                    if job_type in ["facebook_follow", "facebook_page"]:
                                        nhanxu = tds.nhan_xu(job_type+"_cache", code)
                                        #print(nhanxu)
                                        print(f"{status}[{luc}{nhanxu['cache']}/8{do}][{vang}{int(xu):,}{do}]")
                                        if nhanxu['cache'] >= 8:
                                            code = "facebook_api"
                                            sleep(2)
                                            nhanxu = tds.nhan_xu(job_type, code)
                                            if 'error' in nhanxu: print(atuan+do, nhanxu['error'], end='\r'); idx -= 1; doiaccx -= 1; nvblockx -= 1
                                            elif nhanxu.get('success') == 200: xu = nhanxu['data']['xu']; msg = nhanxu['data']['msg']; job_success = nhanxu['data']['job_success']; print(f"{do}[{vang}𝐗{do}][{luc}{gio_vn()}{do}][{xnhac}{status_action}{do}][{luc}Nhận Xu {job_success}/8{do}][{luc}{msg}{do}][{vang}{int(xu):,}{do}]")
                                            else: idx -= 1; doiaccx -= 1; nvblockx -= 1; print(atuan+do, nhanxu, end='\r'); continue
                                    else:
                                        nhanxu = tds.nhan_xu(job_type, code)
                                        if 'error' in nhanxu: print(atuan+do, nhanxu['error'], end='\r'); idx -= 1; doiaccx -= 1; nvblockx -= 1
                                        elif nhanxu.get('success') == 200: xu = nhanxu['data']['xu']; msg = nhanxu['data']['msg']; print(f"{status}[{luc}{msg}{do}][{vang}{int(xu):,}{do}]")
                                        else: idx -= 1; doiaccx -= 1; nvblockx -= 1; print(atuan+do, nhanxu, end='\r'); continue
                                
                                else: idx -= 1; print(status, end='\r'); error_counts[cookie][job_type] = error_counts[cookie].get(job_type, 0) + 1

                                if doiaccx >= doiacc: break
                                if nvblockx >= nvblock: nvblockx = 0; countdown_(delaybl)
                                else: DelayTime(delay)
                            
                            if die_cookie: break  # Thoát khỏi vòng while True nếu cookie die
                            if doiaccx >= doiacc: break
                        except KeyboardInterrupt:
                            raise
                        except Exception as e:
                            print(f"{do}{e}", end="\r")
                    if die_cookie: break  # Thoát khỏi vòng while True nếu cookie die
                    if doiaccx >= doiacc: break
        # Nếu hết cookie hợp lệ
        if not list_clone:
            print(f"{do}Danh sách cookie trống — yêu cầu nhập lại:")
            thanh_ngang()
            list_clone, stt = [], 0
            while True:
                stt += 1
                cookie_fb = input(f'{atuan}Nhập Cookie Facebook Thứ {xnhac}{stt}: {vang}')
                if cookie_fb == '': break
                fb = Facebook_API(cookie_fb)
                if not all([fb.idfb, fb.fb_dtsg, fb.jazoest]): print(f"{atuan}{do}Cookie không hợp lệ hoặc lỗi lấy thông tin."); stt -= 1
                else: print(f"{luc}Id Facebook: {vang}{fb.idfb} {do}</> {luc}Tên Tài Khoản: {vang}{fb.name}"); list_clone.append(cookie_fb); thanh_ngang()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{atuan}{do}Đã dừng chương trình")
        exit