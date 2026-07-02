#!/usr/bin/env python3
"""
Media OS Notion Builder — Creates the complete operating system in a Notion workspace.
Usage: python build_media_os.py --token YOUR_TOKEN --page-id YOUR_PAGE_ID
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
import requests
from typing import Optional, Dict, Any

class NotionBuilder:
    def __init__(self, token: str, parent_page_id: str):
        self.token = token
        self.parent_page_id = parent_page_id
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }
        self.database_ids = {}
        self.created_pages = []

    def request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make a request to the Notion API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                resp = requests.get(url, headers=self.headers, timeout=10)
            elif method == "POST":
                resp = requests.post(url, headers=self.headers, json=data, timeout=10)
            elif method == "PATCH":
                resp = requests.patch(url, headers=self.headers, json=data, timeout=10)
            else:
                raise ValueError(f"Unsupported method: {method}")

            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API Error ({method} {endpoint}): {e}")
            sys.exit(1)

    def create_database(self, title: str, properties: Dict) -> str:
        """Create a database under the parent page."""
        payload = {
            "parent": {"page_id": self.parent_page_id},
            "title": [{"type": "text", "text": {"content": title}}],
            "properties": properties,
        }
        result = self.request("POST", "databases", payload)
        db_id = result["id"]
        self.database_ids[title] = db_id
        print(f"✅ Created database: {title}")
        return db_id

    def create_page(self, parent_id: str, title: str, properties: Dict[str, Any] = None, children: list = None) -> str:
        """Create a page."""
        payload = {
            "parent": {"page_id": parent_id},
            "properties": {
                "title": [{"type": "text", "text": {"content": title}}]
            }
        }
        if properties:
            payload["properties"].update(properties)
        if children:
            payload["children"] = children

        result = self.request("POST", "pages", payload)
        page_id = result["id"]
        self.created_pages.append({"title": title, "id": page_id})
        return page_id

    def add_page_content(self, page_id: str, children: list):
        """Add block content to a page."""
        payload = {"children": children}
        self.request("PATCH", f"blocks/{page_id}/children", payload)

    def build_databases(self):
        """Create all 17 core databases."""
        print("\n📊 Building Databases...\n")

        # 1. People (team directory)
        self.create_database("👥 People", {
            "Name": {"title": {}},
            "Type": {"select": {"options": [
                {"name": "Founder", "color": "red"},
                {"name": "Employee", "color": "blue"},
                {"name": "Freelancer", "color": "green"},
                {"name": "Agency", "color": "purple"},
            ]}},
            "Role": {"multi_select": {"options": [
                {"name": "Editor"}, {"name": "Scriptwriter"}, {"name": "Researcher"},
                {"name": "Thumbnail Designer"}, {"name": "Voice Actor"}, {"name": "Motion GFX"},
            ]}},
            "Status": {"select": {"options": [
                {"name": "Onboarding"}, {"name": "Active"}, {"name": "Bench"}, {"name": "Offboarded"}
            ]}},
            "Email": {"email": {}},
            "Timezone": {"text": {}},
        })

        # 2. Channels
        self.create_database("📺 Channels", {
            "Name": {"title": {}},
            "Code": {"text": {}},
            "Status": {"select": {"options": [
                {"name": "Research"}, {"name": "Pre-launch"}, {"name": "Active"},
                {"name": "Paused"}, {"name": "Sunset"}
            ]}},
            "Vertical": {"select": {"options": [
                {"name": "Business"}, {"name": "History"}, {"name": "Crime"}, {"name": "Religion"},
                {"name": "Science"}, {"name": "Psychology"}, {"name": "Health"}, {"name": "Finance"}
            ]}},
            "Channel URL": {"url": {}},
            "Launch Date": {"date": {}},
            "Channel Lead": {"relation": {"database_id": self.database_ids["👥 People"]}},
            "Upload Schedule": {"text": {}},
            "Target Frequency /mo": {"number": {"precision": 0}},
            "Subscribers (latest)": {"number": {"precision": 0}},
            "Views 30d": {"number": {"precision": 0}},
            "Revenue 30d": {"number": {"precision": 2}},
            "Cost 30d": {"number": {"precision": 2}},
        })

        # 3. Ideas
        self.create_database("💡 Ideas", {
            "Idea": {"title": {}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Status": {"select": {"options": [
                {"name": "Inbox"}, {"name": "Researching"}, {"name": "Scored"},
                {"name": "Approved"}, {"name": "In Production"}, {"name": "Rejected"}, {"name": "Icebox"}
            ]}},
            "Topic": {"text": {}},
            "Niche": {"text": {}},
            "Score": {"number": {"precision": 0}},
            "Priority": {"select": {"options": [
                {"name": "🔥 P1"}, {"name": "P2"}, {"name": "P3"}, {"name": "❄️"}
            ]}},
            "Estimated Views 30d": {"number": {"precision": 0}},
            "CTR Potential": {"number": {"precision": 1}},
            "RPM Potential": {"number": {"precision": 2}},
        })

        # 4. Videos
        self.create_database("🎞 Videos", {
            "Name": {"title": {}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Idea": {"relation": {"database_id": self.database_ids["💡 Ideas"]}},
            "Stage": {"select": {"options": [
                {"name": "💡 Idea"}, {"name": "🔍 Research"}, {"name": "🧱 Outline"},
                {"name": "✍️ Script"}, {"name": "👁 Review"}, {"name": "🎙 Voiceover"},
                {"name": "✂️ Editing"}, {"name": "🖼 Thumbnail"}, {"name": "🏷 Title"},
                {"name": "📝 Description"}, {"name": "🔎 SEO"}, {"name": "✅ QA"},
                {"name": "📅 Scheduled"}, {"name": "🚀 Published"}, {"name": "📈 Performance Review"},
                {"name": "🗄 Archived"}
            ]}},
            "Publish Date": {"date": {}},
            "Length (min)": {"number": {"precision": 1}},
            "Views 30d": {"number": {"precision": 0}},
            "CTR 30d": {"number": {"precision": 2}},
            "Retention %": {"number": {"precision": 1}},
            "Revenue 30d": {"number": {"precision": 2}},
            "Hook Type": {"select": {"options": [
                {"name": "Open Question"}, {"name": "Shocking Fact"}, {"name": "In Media Res"},
                {"name": "Direct Address"}
            ]}},
            "Story Structure": {"select": {"options": [
                {"name": "Classic Hero"}, {"name": "Mystery Box"}, {"name": "Chronological"},
                {"name": "Parallels"}
            ]}},
            "Thumbnail Style": {"select": {"options": [
                {"name": "Face"}, {"name": "Object"}, {"name": "Text-heavy"}, {"name": "High-contrast"}
            ]}},
        })

        # 5. Tasks
        self.create_database("✅ Tasks", {
            "Task": {"title": {}},
            "Status": {"select": {"options": [
                {"name": "Not Started"}, {"name": "In Progress"}, {"name": "In Review"},
                {"name": "Blocked"}, {"name": "Done"}
            ]}},
            "Assignee": {"relation": {"database_id": self.database_ids["👥 People"]}},
            "Due": {"date": {}},
            "Video": {"relation": {"database_id": self.database_ids["🎞 Videos"]}},
            "Stage": {"select": {"options": [
                {"name": "Research"}, {"name": "Script"}, {"name": "Editing"},
                {"name": "Thumbnail"}, {"name": "QA"}, {"name": "Publishing"}
            ]}},
            "Priority": {"select": {"options": [{"name": "P1"}, {"name": "P2"}, {"name": "P3"}]}},
            "Effort (hrs)": {"number": {"precision": 1}},
        })

        # 6. Competitors
        self.create_database("⚔️ Competitors", {
            "Channel": {"title": {}},
            "Channel URL": {"url": {}},
            "Our Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Tier": {"select": {"options": [{"name": "North Star"}, {"name": "Direct"}, {"name": "Emerging"}]}},
            "Subscribers": {"number": {"precision": 0}},
            "Avg Views": {"number": {"precision": 0}},
            "Upload Frequency": {"text": {}},
            "Monetization": {"multi_select": {"options": [
                {"name": "AdSense"}, {"name": "Sponsors"}, {"name": "Affiliate"},
                {"name": "Course"}, {"name": "Merch"}, {"name": "Newsletter"}
            ]}},
        })

        # 7. Competitor Videos
        self.create_database("🎯 Competitor Videos", {
            "Title": {"title": {}},
            "URL": {"url": {}},
            "Competitor": {"relation": {"database_id": self.database_ids["⚔️ Competitors"]}},
            "Views": {"number": {"precision": 0}},
            "Age (days)": {"number": {"precision": 0}},
            "Outlier Ratio": {"number": {"precision": 2}},
            "Why It Worked": {"text": {}},
        })

        # 8. Sponsors CRM
        self.create_database("🏢 Companies", {
            "Company": {"title": {}},
            "URL": {"url": {}},
            "Category": {"select": {"options": [
                {"name": "VPN"}, {"name": "SaaS"}, {"name": "Finance"}, {"name": "Education"},
                {"name": "DTC"}, {"name": "Gaming"}, {"name": "Health"}
            ]}},
            "Fit Channels": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Status": {"select": {"options": [
                {"name": "Prospect"}, {"name": "Contacted"}, {"name": "In Conversation"},
                {"name": "Active"}, {"name": "Churned"}
            ]}},
        })

        # 9. Deals
        self.create_database("💰 Deals", {
            "Deal": {"title": {}},
            "Company": {"relation": {"database_id": self.database_ids["🏢 Companies"]}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Stage": {"select": {"options": [
                {"name": "Lead"}, {"name": "Pitched"}, {"name": "Negotiating"},
                {"name": "Verbal"}, {"name": "Won"}, {"name": "Lost"}
            ]}},
            "Value": {"number": {"precision": 2}},
            "Close Date": {"date": {}},
        })

        # 10. SOPs
        self.create_database("📖 SOP Library", {
            "SOP": {"title": {}},
            "Version": {"text": {}},
            "Status": {"select": {"options": [
                {"name": "Draft"}, {"name": "Active"}, {"name": "Needs Update"}, {"name": "Deprecated"}
            ]}},
            "Category": {"select": {"options": [
                {"name": "Research"}, {"name": "Script"}, {"name": "Editing"},
                {"name": "Thumbnail"}, {"name": "QA"}, {"name": "Publishing"},
                {"name": "Analytics"}, {"name": "Hiring"}
            ]}},
            "Owner": {"relation": {"database_id": self.database_ids["👥 People"]}},
            "Time to Execute (min)": {"number": {"precision": 0}},
        })

        # 11. Prompts
        self.create_database("🤖 Prompts", {
            "Prompt": {"title": {}},
            "Version": {"text": {}},
            "Status": {"select": {"options": [
                {"name": "Draft"}, {"name": "Testing"}, {"name": "Active"}, {"name": "Deprecated"}
            ]}},
            "Category": {"select": {"options": [
                {"name": "Research"}, {"name": "Script"}, {"name": "Hooks"},
                {"name": "Thumbnails"}, {"name": "SEO"}, {"name": "Analytics"},
                {"name": "Competitor"}, {"name": "Outreach"}
            ]}},
            "Owner": {"relation": {"database_id": self.database_ids["👥 People"]}},
        })

        # 12. Assets
        self.create_database("🎨 Assets", {
            "Asset": {"title": {}},
            "Type": {"select": {"options": [
                {"name": "Logo"}, {"name": "Font"}, {"name": "Music"}, {"name": "SFX"},
                {"name": "B-roll"}, {"name": "Animation"}, {"name": "Template"}
            ]}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "File Link": {"url": {}},
            "License Type": {"select": {"options": [
                {"name": "Owned"}, {"name": "Commissioned"}, {"name": "Royalty-free"},
                {"name": "Licensed"}, {"name": "Creative Commons"}, {"name": "Fair-use"}
            ]}},
            "License Expiry": {"date": {}},
        })

        # 13. Knowledge Base
        self.create_database("🧠 Knowledge Base", {
            "Entry": {"title": {}},
            "Type": {"select": {"options": [
                {"name": "Book"}, {"name": "Course"}, {"name": "Lesson Learned"},
                {"name": "Industry Report"}, {"name": "Framework"}
            ]}},
            "Topic": {"multi_select": {"options": [
                {"name": "Storytelling"}, {"name": "Packaging"}, {"name": "Retention"},
                {"name": "SEO"}, {"name": "Monetization"}, {"name": "Hiring"}
            ]}},
            "Channel Relevance": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Source": {"url": {}},
            "Added By": {"relation": {"database_id": self.database_ids["👥 People"]}},
        })

        # 14. OKRs
        self.create_database("🎯 Objectives", {
            "Objective": {"title": {}},
            "Quarter": {"text": {}},
            "Owner": {"relation": {"database_id": self.database_ids["👥 People"]}},
            "Status": {"select": {"options": [
                {"name": "On Track"}, {"name": "At Risk"}, {"name": "Off Track"}, {"name": "Done"}
            ]}},
        })

        # 15. Key Results
        self.create_database("📏 Key Results", {
            "Key Result": {"title": {}},
            "Objective": {"relation": {"database_id": self.database_ids["🎯 Objectives"]}},
            "Target": {"text": {}},
            "Current": {"text": {}},
            "Owner": {"relation": {"database_id": self.database_ids["👥 People"]}},
        })

        # 16. Metrics Snapshots
        self.create_database("📸 Channel Snapshots", {
            "Snapshot": {"title": {}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Week Of": {"date": {}},
            "Subscribers": {"number": {"precision": 0}},
            "Views 28d": {"number": {"precision": 0}},
            "CTR 28d": {"number": {"precision": 2}},
            "RPM": {"number": {"precision": 2}},
            "Avg % Viewed": {"number": {"precision": 1}},
        })

        # 17. Meetings
        self.create_database("🤝 Meetings", {
            "Meeting": {"title": {}},
            "Type": {"select": {"options": [
                {"name": "Weekly Sync"}, {"name": "Monthly Review"},
                {"name": "Quarterly Planning"}, {"name": "Retro"}
            ]}},
            "Date": {"date": {}},
            "Attendees": {"relation": {"database_id": self.database_ids["👥 People"]}},
        })

        # 18. Hiring
        self.create_database("🎯 Applicants", {
            "Name": {"title": {}},
            "Role": {"select": {"options": [
                {"name": "Editor"}, {"name": "Thumbnail Designer"}, {"name": "Voice Actor"},
                {"name": "Scriptwriter"}, {"name": "Researcher"}
            ]}},
            "Stage": {"select": {"options": [
                {"name": "Sourced"}, {"name": "Applied"}, {"name": "Screened"},
                {"name": "Interview"}, {"name": "Trial"}, {"name": "Hired"}, {"name": "Rejected"}
            ]}},
            "Email": {"email": {}},
            "Portfolio": {"url": {}},
            "Rate": {"number": {"precision": 2}},
        })

        # 19. Finance - Revenue
        self.create_database("📈 Revenue", {
            "Entry": {"title": {}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Stream": {"select": {"options": [
                {"name": "AdSense"}, {"name": "Sponsorship"}, {"name": "Affiliate"},
                {"name": "Course"}, {"name": "Merch"}, {"name": "Licensing"}
            ]}},
            "Amount": {"number": {"precision": 2}},
            "Month": {"date": {}},
        })

        # 20. Finance - Expenses
        self.create_database("📉 Expenses", {
            "Entry": {"title": {}},
            "Channel": {"relation": {"database_id": self.database_ids["📺 Channels"]}},
            "Category": {"select": {"options": [
                {"name": "Freelancer"}, {"name": "Software"}, {"name": "Music & Assets"},
                {"name": "Ads"}, {"name": "Equipment"}
            ]}},
            "Video": {"relation": {"database_id": self.database_ids["🎞 Videos"]}},
            "Amount": {"number": {"precision": 2}},
            "Date": {"date": {}},
        })

        # 21. Automations
        self.create_database("⚙️ Automations", {
            "Automation": {"title": {}},
            "Status": {"select": {"options": [
                {"name": "Live"}, {"name": "Paused"}, {"name": "Broken"}, {"name": "Planned"}
            ]}},
            "Tool": {"select": {"options": [
                {"name": "Notion"}, {"name": "Make"}, {"name": "n8n"}, {"name": "Zapier"}
            ]}},
            "Owner": {"relation": {"database_id": self.database_ids["👥 People"]}},
            "Last Verified": {"date": {}},
        })

    def seed_data(self):
        """Add seed content."""
        print("\n🌱 Adding Seed Content...\n")

        # Add founders to People
        people_db = self.database_ids["👥 People"]
        founders = [
            {"name": "Founder 1 (CEO)", "role": ["Strategy", "Analytics", "Hiring"]},
            {"name": "Founder 2 (Growth)", "role": ["Sales", "Monetization", "Recruiting"]},
            {"name": "Founder 3 (Production)", "role": ["Scripts", "Editing", "QC"]},
        ]
        for founder in founders:
            self.request("POST", "pages", {
                "parent": {"database_id": people_db},
                "properties": {
                    "Name": {"title": [{"type": "text", "text": {"content": founder["name"]}}]},
                    "Type": {"select": {"name": "Founder"}},
                }
            })
            print(f"✅ Added: {founder['name']}")

        # Add Q3 2026 objectives
        obj_db = self.database_ids["🎯 Objectives"]
        objectives = [
            "Prove channel #2 with 12+ videos",
            "Hit $X revenue target",
            "Build the SOP library to production-ready",
        ]
        for obj in objectives:
            self.request("POST", "pages", {
                "parent": {"database_id": obj_db},
                "properties": {
                    "Objective": {"title": [{"type": "text", "text": {"content": obj}}]},
                    "Quarter": {"select": {"name": "Q3 2026"}},
                }
            })
            print(f"✅ Added objective: {obj}")

    def create_dashboards(self):
        """Create dashboard pages with linked views."""
        print("\n📊 Creating Dashboards...\n")

        dashboards = [
            {
                "title": "🏛 Company HQ",
                "description": "Mission, scoreboard, projects, announcements",
                "parent": self.parent_page_id,
            },
            {
                "title": "🧠 CEO Dashboard",
                "description": "Strategy, ideas, analytics, hiring",
                "parent": self.parent_page_id,
            },
            {
                "title": "📈 Growth Dashboard",
                "description": "Deals, outreach, sponsors, metrics",
                "parent": self.parent_page_id,
            },
            {
                "title": "🎬 Production Dashboard",
                "description": "Factory, pipeline, assets, team load",
                "parent": self.parent_page_id,
            },
            {
                "title": "📊 Analytics Dashboard",
                "description": "Trends, cohorts, performance analysis",
                "parent": self.parent_page_id,
            },
        ]

        for dashboard in dashboards:
            page_id = self.create_page(
                dashboard["parent"],
                dashboard["title"],
            )
            self.add_page_content(page_id, [
                {
                    "object": "block",
                    "type": "callout",
                    "callout": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": f"📘 {dashboard['description']} — Populate with linked database views per the dashboard spec in the repo."
                            }
                        }],
                        "icon": {"type": "emoji", "emoji": "🚀"}
                    }
                }
            ])
            print(f"✅ Created dashboard: {dashboard['title']}")

    def build(self):
        """Run the full build."""
        print("=" * 60)
        print("🚀 NOTION MEDIA OS BUILDER")
        print("=" * 60)

        self.build_databases()
        self.seed_data()
        self.create_dashboards()

        print("\n" + "=" * 60)
        print("✅ BUILD COMPLETE")
        print("=" * 60)
        print(f"\n📊 Created {len(self.database_ids)} databases")
        print(f"📄 Created {len(self.created_pages)} pages")
        print(f"\n🎯 Next steps:")
        print(f"   1. Wire up database relations in Notion UI")
        print(f"   2. Create database views per the dashboard specs")
        print(f"   3. Add database templates for New Video, New Channel")
        print(f"   4. Set up automations (Make/n8n)")
        print(f"\nAll specs and SOPs are in the repo: /home/user/Notion/")

def main():
    parser = argparse.ArgumentParser(description="Build Media OS in Notion")
    parser.add_argument("--token", required=True, help="Notion integration token")
    parser.add_argument("--page-id", required=True, help="Parent page ID (the trio)")
    args = parser.parse_args()

    builder = NotionBuilder(args.token, args.page_id)
    builder.build()

if __name__ == "__main__":
    main()
